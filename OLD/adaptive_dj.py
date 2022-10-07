import glob

print('filename', 'J0_count', 'J1_count', 'J2_count', 'D0J0_count', 'D0J1_count', 'D0J2_count', 'D1J0_count', 'D1J1_count', 'D1J2_count', 
      'D2J0_count', 'D2J1_count', 'D2J2_count', 'J1/J2', 
      'TCRBJ01-01', 'TCRBJ01-02', 'TCRBJ01-03', 'TCRBJ01-04', 'TCRBJ01-05', 'TCRBJ01-06',
      'TCRBJ02-01', 'TCRBJ02-02', 'TCRBJ02-03', 'TCRBJ02-04', 'TCRBJ02-05', 'TCRBJ02-06', 'TCRBJ02-07',
      sep=',')


for filename in glob.glob('*tsv'):

    j0_count, j1_count, j2_count = [0, 0, 0]
    d0j0_count, d0j1_count, d0j2_count = [0, 0, 0]
    d1j0_count, d1j1_count, d1j2_count = [0, 0, 0]
    d2j0_count, d2j1_count, d2j2_count = [0, 0, 0]

    jgene_count = {'TCRBJ01-01':0, 'TCRBJ01-02':0, 'TCRBJ01-03':0, 'TCRBJ01-04':0, 'TCRBJ01-05':0, 'TCRBJ01-06':0, 
                   'TCRBJ02-01':0, 'TCRBJ02-02':0, 'TCRBJ02-03':0, 'TCRBJ02-04':0, 'TCRBJ02-05':0, 'TCRBJ02-06':0, 'TCRBJ02-07':0}
    
    with open(filename) as f:
        f.readline()
        for line in f:
            fields = line.split(sep='\t')

            # Format from manually downloaded files
            #dfamily = fields[13]
            #jfamily = fields[20]

            # Format from Emerson paper data set
            dfamily = fields[12]
            jfamily = fields[15]
            jgene = fields[16]

            if 'TCRBJ' in jgene:
                jgene_count[jgene] += 1

            if not dfamily:
                dfamily = 'd_undef'

            if not jfamily:
                jfamily = 'j_undef'

            if jfamily == 'j_undef':
                j0_count += 1
            elif jfamily == 'TCRBJ01':
                j1_count += 1
            elif jfamily == 'TCRBJ02':
                j2_count += 1

            if dfamily == 'd_undef' and jfamily == 'j_undef':
                d0j0_count += 1
            elif dfamily == 'd_undef' and jfamily == 'TCRBJ01':
                d0j1_count += 1
            elif dfamily == 'd_undef' and jfamily == 'TCRBJ02':
                d0j2_count += 1
            elif dfamily == 'TCRBD01' and jfamily == 'j_undef':
                d1j0_count += 1
            elif dfamily == 'TCRBD01' and jfamily == 'TCRBJ01':
                d1j1_count += 1
            elif dfamily == 'TCRBD01' and jfamily == 'TCRBJ02':
                d1j2_count += 1
            elif dfamily == 'TCRBD02' and jfamily == 'j_undef':
                d2j0_count += 1
            elif dfamily == 'TCRBD02' and jfamily == 'TCRBJ01':
                d2j1_count += 1
            elif dfamily == 'TCRBD02' and jfamily == 'TCRBJ02':
                d2j2_count += 1

        j1_j2_ratio = j1_count / j2_count

        jgene_count['TCRBJ01-01'] = jgene_count['TCRBJ01-01'] / j1_count
        jgene_count['TCRBJ01-02'] = jgene_count['TCRBJ01-02'] / j1_count
        jgene_count['TCRBJ01-03'] = jgene_count['TCRBJ01-03'] / j1_count
        jgene_count['TCRBJ01-04'] = jgene_count['TCRBJ01-04'] / j1_count
        jgene_count['TCRBJ01-05'] = jgene_count['TCRBJ01-05'] / j1_count
        jgene_count['TCRBJ01-06'] = jgene_count['TCRBJ01-06'] / j1_count
        jgene_count['TCRBJ02-01'] = jgene_count['TCRBJ02-01'] / j2_count
        jgene_count['TCRBJ02-02'] = jgene_count['TCRBJ02-02'] / j2_count
        jgene_count['TCRBJ02-03'] = jgene_count['TCRBJ02-03'] / j2_count
        jgene_count['TCRBJ02-04'] = jgene_count['TCRBJ02-04'] / j2_count
        jgene_count['TCRBJ02-05'] = jgene_count['TCRBJ02-05'] / j2_count
        jgene_count['TCRBJ02-06'] = jgene_count['TCRBJ02-06'] / j2_count
        jgene_count['TCRBJ02-07'] = jgene_count['TCRBJ02-07'] / j2_count

        print(filename, j0_count, j1_count, j2_count, d0j0_count, d0j1_count, d0j2_count, 
              d1j0_count, d1j1_count, d1j2_count, d2j0_count, d2j1_count, d2j2_count, j1_j2_ratio, 
              jgene_count['TCRBJ01-01'], jgene_count['TCRBJ01-02'], jgene_count['TCRBJ01-03'], jgene_count['TCRBJ01-04'], 
              jgene_count['TCRBJ01-05'], jgene_count['TCRBJ01-06'],
              jgene_count['TCRBJ02-01'], jgene_count['TCRBJ02-02'], jgene_count['TCRBJ02-03'], jgene_count['TCRBJ02-04'], 
              jgene_count['TCRBJ02-05'], jgene_count['TCRBJ02-06'], jgene_count['TCRBJ02-07'],
              sep=',')

