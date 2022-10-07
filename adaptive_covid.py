import glob

print('filename', 'J0_count', 'J1_count', 'J2_count', 'J1/J2', 
      'TCRBJ01-01', 'TCRBJ01-02', 'TCRBJ01-03', 'TCRBJ01-04', 'TCRBJ01-05', 'TCRBJ01-06',
      'TCRBJ02-01', 'TCRBJ02-02', 'TCRBJ02-03', 'TCRBJ02-04', 'TCRBJ02-05', 'TCRBJ02-06', 'TCRBJ02-07',
      'TCRBJ01-01-norm', 'TCRBJ01-02-norm', 'TCRBJ01-03-norm', 'TCRBJ01-04-norm', 'TCRBJ01-05-norm', 'TCRBJ01-06-norm',
      'TCRBJ02-01-norm', 'TCRBJ02-02-norm', 'TCRBJ02-03-norm', 'TCRBJ02-04-norm', 'TCRBJ02-05-norm', 'TCRBJ02-06-norm', 'TCRBJ02-07-norm',
      sep=',')


for filename in glob.glob('*tsv'):

    j0_count, j1_count, j2_count = [0, 0, 0]

    jgene_count = {'TCRBJ01-01':0, 'TCRBJ01-02':0, 'TCRBJ01-03':0, 'TCRBJ01-04':0, 'TCRBJ01-05':0, 'TCRBJ01-06':0, 
                   'TCRBJ02-01':0, 'TCRBJ02-02':0, 'TCRBJ02-03':0, 'TCRBJ02-04':0, 'TCRBJ02-05':0, 'TCRBJ02-06':0, 'TCRBJ02-07':0}
    
    with open(filename) as f:
        f.readline()
        for line in f:
            fields = line.split(sep='\t')

            # Format from COVID data set
            jfamily = fields[40]
            jgene = fields[42]

            if not jfamily:
                jfamily = 'j_undef'

            if jfamily == 'j_undef':
                j0_count += 1
            elif jfamily == 'TCRBJ01':
                j1_count += 1
            elif jfamily == 'TCRBJ02':
                j2_count += 1

            if 'TCRBJ' in jgene:
                jgene_count[jgene] += 1

        j1_j2_ratio = j1_count / j2_count

        jgene_count['TCRBJ01-01-norm'] = jgene_count['TCRBJ01-01'] / j1_count
        jgene_count['TCRBJ01-02-norm'] = jgene_count['TCRBJ01-02'] / j1_count
        jgene_count['TCRBJ01-03-norm'] = jgene_count['TCRBJ01-03'] / j1_count
        jgene_count['TCRBJ01-04-norm'] = jgene_count['TCRBJ01-04'] / j1_count
        jgene_count['TCRBJ01-05-norm'] = jgene_count['TCRBJ01-05'] / j1_count
        jgene_count['TCRBJ01-06-norm'] = jgene_count['TCRBJ01-06'] / j1_count
        jgene_count['TCRBJ02-01-norm'] = jgene_count['TCRBJ02-01'] / j2_count
        jgene_count['TCRBJ02-02-norm'] = jgene_count['TCRBJ02-02'] / j2_count
        jgene_count['TCRBJ02-03-norm'] = jgene_count['TCRBJ02-03'] / j2_count
        jgene_count['TCRBJ02-04-norm'] = jgene_count['TCRBJ02-04'] / j2_count
        jgene_count['TCRBJ02-05-norm'] = jgene_count['TCRBJ02-05'] / j2_count
        jgene_count['TCRBJ02-06-norm'] = jgene_count['TCRBJ02-06'] / j2_count
        jgene_count['TCRBJ02-07-norm'] = jgene_count['TCRBJ02-07'] / j2_count

        print(filename, j0_count, j1_count, j2_count, j1_j2_ratio, 
              jgene_count['TCRBJ01-01'], jgene_count['TCRBJ01-02'], jgene_count['TCRBJ01-03'], jgene_count['TCRBJ01-04'], 
              jgene_count['TCRBJ01-05'], jgene_count['TCRBJ01-06'],
              jgene_count['TCRBJ02-01'], jgene_count['TCRBJ02-02'], jgene_count['TCRBJ02-03'], jgene_count['TCRBJ02-04'], 
              jgene_count['TCRBJ02-05'], jgene_count['TCRBJ02-06'], jgene_count['TCRBJ02-07'],
              jgene_count['TCRBJ01-01-norm'], jgene_count['TCRBJ01-02-norm'], jgene_count['TCRBJ01-03-norm'], jgene_count['TCRBJ01-04-norm'], 
              jgene_count['TCRBJ01-05-norm'], jgene_count['TCRBJ01-06-norm'],
              jgene_count['TCRBJ02-01-norm'], jgene_count['TCRBJ02-02-norm'], jgene_count['TCRBJ02-03-norm'], jgene_count['TCRBJ02-04-norm'], 
              jgene_count['TCRBJ02-05-norm'], jgene_count['TCRBJ02-06-norm'], jgene_count['TCRBJ02-07-norm'],
              sep=',')

