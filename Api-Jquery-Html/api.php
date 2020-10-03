<?php
include 'koneksi.php';


/**
 * Initial data array
 */

$data = array();
$data_total_kinerja = array();
$data_indikator = array();

/**
 * Query get total kinerja each kode subindikator
 */

$query_total_kinerja = $db->query("SELECT A.kode_subindikator, SUM(A.nilai) AS nilai_total FROM `data_kinerja` AS A INNER JOIN `data_sub_indikator` AS B ON(A.kode_subindikator = B.kode_subindikator) GROUP BY B.kode_subindikator ORDER BY B.subindikator_id ASC");
while ($result_total_kinerja = $query_total_kinerja->fetch_assoc()) {
    $data_total_kinerja[$result_total_kinerja['kode_subindikator']] = $result_total_kinerja['nilai_total'];
}

/**
 * Query get procentage each indikator
 */

$query_indikator = $db->query("SELECT * FROM data_indikator");
while ($result_indikator = $query_indikator->fetch_assoc()) {
    $data_indikator[$result_indikator['kode_indikator']] = $result_indikator['bobot'];
}

/**
 * Initial data sub indokator
 */

$index_sub_indikator = 0;
$query_subindikator = $db->query("SELECT * FROM data_sub_indikator");
while ($result_subindikator = $query_subindikator->fetch_assoc()) {
    $data['data_subindikator'][$index_sub_indikator]['kode_subindikator'] = $result_subindikator['kode_subindikator'];
    $data['data_subindikator'][$index_sub_indikator]['subindikator'] = $result_subindikator['subindikator'];

    $index_sub_indikator++;
}

/**
 * Initial index for karyawan
 */

$index_karyawan = 0;

/**
 * Begin query from database
 */

$query_karyawan = $db->query('SELECT * FROM data_karyawan');
while ($result_karyawan = $query_karyawan->fetch_assoc()) {

    /**
     * Set value into array json
     */

    $data['detail_karyawan'][$index_karyawan]['karyawan']['id'] = $result_karyawan['karyawan_id'];
    $data['detail_karyawan'][$index_karyawan]['karyawan']['name'] = $result_karyawan['nama'];


    /**
     * Initial index for kinerja
     */

    $index_kinerja = 0;

    /**
     * Initiate percentage us & nc
     */

    $percentage_us = 0;
    $percentage_nc = 0;

    $data_allow_kode_subindikator_us = ['US'];
    $data_allow_kode_subindikator_nc = ['NC'];

    /**
     * Inititate value Pelatihan/Training
     */

    $total_value_pelatihan_training = 0;
    $total_data_pelatihan_training = 0;
    $data_allow_kode_subindikator_pelatihan = ['ST', 'CT', 'TT', 'FT', 'PT'];

    /**
     * Initiate variable LAP
     */

    $nilai_lap = 0;
    $data_allow_kode_subindikator_lap = ['LA'];

    /**
     * Query data from kinerja
     */

    $query_kinerja = $db->query("SELECT A.*, B.subindikator FROM data_kinerja AS A INNER JOIN data_sub_indikator AS B ON(A.kode_subindikator = B.kode_subindikator) WHERE id_karyawan = '$result_karyawan[karyawan_id]'");
    while ($result_kinerja = $query_kinerja->fetch_assoc()) {

        /**
         * Set value into data kinerja each karyawan
         */

        $data['detail_karyawan'][$index_karyawan]['kinerja'][$index_kinerja]['nilai'] = $result_kinerja['nilai'];
        $data['detail_karyawan'][$index_karyawan]['kinerja'][$index_kinerja]['kode_subindikator'] = $result_kinerja['kode_subindikator'];
        $data['detail_karyawan'][$index_karyawan]['kinerja'][$index_kinerja]['subindikator'] = $result_kinerja['subindikator'];

        /**
         * Calculate Percentage %US & %NC
         */

        if (in_array($result_kinerja['kode_subindikator'], $data_allow_kode_subindikator_us)) $percentage_us = $result_kinerja['nilai'] / $data_total_kinerja['US'];
        if (in_array($result_kinerja['kode_subindikator'], $data_allow_kode_subindikator_nc)) $percentage_nc = $result_kinerja['nilai'] / $data_total_kinerja['NC'];

        /**
         * Calculate for Pelatihan/Training
         */

        if (in_array($result_kinerja['kode_subindikator'], $data_allow_kode_subindikator_pelatihan)) {
            $total_value_pelatihan_training += $result_kinerja['nilai'];
            $total_data_pelatihan_training++;
        }

        /**
         * Calculate for Code LAP
         */

        if (in_array($result_kinerja['kode_subindikator'], $data_allow_kode_subindikator_lap)) $nilai_lap = $result_kinerja['nilai'] / 100;

        $index_kinerja++;
    }

    /**
     * Set array US & NC
     */

    //  if di round
    // $data[$index_karyawan]['nilai_us'] = round($percentage_us, 9);
    // $data[$index_karyawan]['nilai_nc'] = round($percentage_nc, 9);
    // else round

    $data['detail_karyawan'][$index_karyawan]['nilai_us'] = $percentage_us;
    $data['detail_karyawan'][$index_karyawan]['nilai_nc'] = $percentage_nc;

    /**
     * Calculate value PEJ
     */

    $nilai_pej = ($percentage_us + $percentage_nc) / 2;
    $data['detail_karyawan'][$index_karyawan]['nilai_pej'] = $nilai_pej;

    /**
     * Calculate Value PEL
     */

    $nilai_pel = ($total_data_pelatihan_training > 0) ? $total_value_pelatihan_training / $total_data_pelatihan_training : 0;
    $data['detail_karyawan'][$index_karyawan]['nilai_pel'] = $nilai_pel;

    /**
     * Caculate value LAP into array
     */

    $data['detail_karyawan'][$index_karyawan]['nilai_lap'] = $nilai_lap;

    /**
     * Calculate total from indikator
     */

    // karena data di db salah maka pakai manual
    // Menghitung berdasarkan data di db 
    // $total_pej = $nilai_pej*$data_indikator['PEJ'];
    // $total_pel = $nilai_pel*$data_indikator['PEL'];
    // $total_lap = $nilai_lap*$data_indikator['LAP'];

    $total_pej = $nilai_pej * 20;
    $total_pel = $nilai_pel * 30;
    $total_lap = $nilai_lap * 50;
    $total_global = $total_pej + $total_pel + $total_lap;

    $data['detail_karyawan'][$index_karyawan]['total_global'] = $total_global;


    $index_karyawan++;
}

echo json_encode($data);
