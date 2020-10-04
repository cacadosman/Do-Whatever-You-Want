$.ajax({
    dataType: 'json',
    url: 'http://localhost:8001/api.php',
    success: function (data) {

        let data_subindikator = data.data_subindikator;
        let detail_karyawan = data.detail_karyawan;
        // console.log(detail_karyawan);

        let html = '';

        html += '<table border="1" cellpadding="0" cellspacing="0">';
        html += '   <thead>';
        html += '       <tr>';
        html += '           <th rowspan="3">No.</th>';
        html += '           <th rowspan="3">Nama</th>';
        html += '           <th colspan="' + data_subindikator.length + '">NILAI SUBINDIKATOR</th>';
        html += '           <th colspan="5">NILAI INDIKATOR</th>';
        html += '           <th rowspan="3">TOTAL</th>';
        html += '       </tr>';

        html += '<tr>';
        data_subindikator.forEach(resultSubindikator => {
            html += '   <th> ' + resultSubindikator.subindikator + ' </th>';
        });
        html += '   <th colspan="3">Penjualan / Sales</th>';
        html += '   <th>Pelatihan / Training</th>';
        html += '   <th>Laporan</th>';
        html += '</tr>';

        html += '<tr>';
        data_subindikator.forEach(resultSubindikator => {
            html += '   <th> ' + resultSubindikator.kode_subindikator + ' </th>';
        });
        html += '   <th>% US</th>';
        html += '   <th>% NC</th>';
        html += '   <th>PEJ</th>';
        html += '   <th>PEL</th>';
        html += '   <th>LAP</th>';
        html += '</tr>';

        html += '   </thead>';


        html += '   <tbody>';
        let no = 1;
        detail_karyawan.forEach(dataKaryawan => {
            let karyawanName = dataKaryawan.karyawan.name;
            html += '<tr>';
            html += '   <td align="center"> ' + no + ' </td>';
            html += '   <td> ' + karyawanName + ' </td>';

            data_subindikator.forEach(resultSubindikator => {
                let indexKinerjaFix = 0;
                for (keyKinjera in dataKaryawan.kinerja) {
                    if (dataKaryawan.kinerja.hasOwnProperty(keyKinjera) && dataKaryawan.kinerja[keyKinjera].kode_subindikator == resultSubindikator.kode_subindikator) {
                        indexKinerjaFix = keyKinjera;
                        break;
                    }
                }

                let karyawanKinerja = (typeof dataKaryawan.kinerja !== 'undefined') ? dataKaryawan.kinerja[indexKinerjaFix] : '';

                let kinerjaNilai = (typeof karyawanKinerja.nilai === 'undefined') ? '' : karyawanKinerja.nilai;

                html += '<td align="center">' + kinerjaNilai + '</td>';

            });

            let nilaiUs = (dataKaryawan.nilai_us > 0) ? dataKaryawan.nilai_us.toFixed(9) : '';
            let nilaiNc = (dataKaryawan.nilai_nc > 0) ? dataKaryawan.nilai_nc.toFixed(9) : '';
            let nilaiPej = (dataKaryawan.nilai_pej > 0) ? dataKaryawan.nilai_pej.toFixed(9) : '';
            let nilaiPel = (dataKaryawan.nilai_pel > 0) ? dataKaryawan.nilai_pel.toFixed(9) : '';
            let nilaiLap = (dataKaryawan.nilai_lap > 0) ? dataKaryawan.nilai_lap.toFixed(9) : '';
            let nilaiGlobal = (dataKaryawan.total_global > 0) ? dataKaryawan.total_global.toFixed(9) : '';

            html += '   <td align="center">' + nilaiUs + '</td>';
            html += '   <td align="center">' + nilaiNc + '</td>';
            html += '   <td align="center">' + nilaiPej + '</td>';
            html += '   <td align="center">' + nilaiPel + '</td>';
            html += '   <td align="center">' + nilaiLap + '</td>';
            html += '   <td align="center">' + nilaiGlobal + '</td>';

            html += '</tr>';

            no++;
        });


        html += '   </tbody>';
        html += '</table>';

        $('.data-render').html(html);
    },
    error: function (data) {
        console.log(data);
    },
});