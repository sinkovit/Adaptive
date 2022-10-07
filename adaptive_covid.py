import glob

print('filename', 'J0_count', 'J1_count', 'J2_count', 'J1/J2', 
      'TCRBJ01-01', 'TCRBJ01-02', 'TCRBJ01-03', 'TCRBJ01-04', 'TCRBJ01-05', 'TCRBJ01-06',
      'TCRBJ02-01', 'TCRBJ02-02', 'TCRBJ02-03', 'TCRBJ02-04', 'TCRBJ02-05', 'TCRBJ02-06', 'TCRBJ02-07',
      'TCRBJ-other',
      'TCRBJ01-01/j1j2', 'TCRBJ01-02/j1j2', 'TCRBJ01-03/j1j2', 'TCRBJ01-04/j1j2', 'TCRBJ01-05/j1j2', 'TCRBJ01-06/j1j2',
      'TCRBJ02-01/j1j2', 'TCRBJ02-02/j1j2', 'TCRBJ02-03/j1j2', 'TCRBJ02-04/j1j2', 'TCRBJ02-05/j1j2', 'TCRBJ02-06/j1j2', 'TCRBJ02-07/j1j2',
      'TCRBJ-other/j1j2',
      'TCRBJ01-01/j1', 'TCRBJ01-02/j1', 'TCRBJ01-03/j1', 'TCRBJ01-04/j1', 'TCRBJ01-05/j1', 'TCRBJ01-06/j1',
      'TCRBJ02-01/j2', 'TCRBJ02-02/j2', 'TCRBJ02-03/j2', 'TCRBJ02-04/j2', 'TCRBJ02-05/j2', 'TCRBJ02-06/j2', 'TCRBJ02-07/j2',
      sep=',')

for filename in glob.glob('ImmuneCODE-Review-002/*.tsv'):

    # J gene families (j0_count is grab bag for anything not TCRBJ01 or TCRBJ01)
    j0_count, j1_count, j2_count = [0, 0, 0]

    # J genes (TCRBJ_other is grab bag for anythong other than TCRBJ01-0[1-6] or TCRBJ02-0[1-7]
    TCRBJ_other = 0
    jgene_count = {'TCRBJ01-01':0, 'TCRBJ01-02':0, 'TCRBJ01-03':0, 'TCRBJ01-04':0, 'TCRBJ01-05':0, 'TCRBJ01-06':0, 
                   'TCRBJ02-01':0, 'TCRBJ02-02':0, 'TCRBJ02-03':0, 'TCRBJ02-04':0, 'TCRBJ02-05':0, 'TCRBJ02-06':0, 'TCRBJ02-07':0}

    lineno = 0
    with open(filename) as f:
        f.readline()
        for line in f:
            lineno += 1
            fields = line.split(sep='\t')

            # Format from COVID data set
            jfamily = fields[40]
            jgene = fields[42]

            if jfamily == 'TCRBJ01':
                j1_count +=1
            elif jfamily == 'TCRBJ02':
                j2_count +=1
            else:
                j0_count +=1
                
            if jgene in jgene_count.keys():
                jgene_count[jgene] += 1
            else:
                TCRBJ_other += 1

        j1j2_count = j1_count + j2_count
        j1j2_ratio = j1_count / j2_count

        print(filename, j0_count, j1_count, j2_count, j1j2_ratio, 
              jgene_count['TCRBJ01-01'], jgene_count['TCRBJ01-02'],
              jgene_count['TCRBJ01-03'], jgene_count['TCRBJ01-04'], 
              jgene_count['TCRBJ01-05'], jgene_count['TCRBJ01-06'],
              jgene_count['TCRBJ02-01'], jgene_count['TCRBJ02-02'],
              jgene_count['TCRBJ02-03'], jgene_count['TCRBJ02-04'], 
              jgene_count['TCRBJ02-05'], jgene_count['TCRBJ02-06'],
              jgene_count['TCRBJ02-07'],
              TCRBJ_other,
              jgene_count['TCRBJ01-01']/j1j2_count, jgene_count['TCRBJ01-02']/j1j2_count,
              jgene_count['TCRBJ01-03']/j1j2_count, jgene_count['TCRBJ01-04']/j1j2_count,
              jgene_count['TCRBJ01-05']/j1j2_count, jgene_count['TCRBJ01-06']/j1j2_count,
              jgene_count['TCRBJ02-01']/j1j2_count, jgene_count['TCRBJ02-02']/j1j2_count,
              jgene_count['TCRBJ02-03']/j1j2_count, jgene_count['TCRBJ02-04']/j1j2_count, 
              jgene_count['TCRBJ02-05']/j1j2_count, jgene_count['TCRBJ02-06']/j1j2_count,
              jgene_count['TCRBJ02-07']/j1j2_count,
              TCRBJ_other/j1j2_count,
              jgene_count['TCRBJ01-01']/j1_count, jgene_count['TCRBJ01-02']/j1_count,
              jgene_count['TCRBJ01-03']/j1_count, jgene_count['TCRBJ01-04']/j1_count, 
              jgene_count['TCRBJ01-05']/j1_count, jgene_count['TCRBJ01-06']/j1_count,
              jgene_count['TCRBJ02-01']/j2_count, jgene_count['TCRBJ02-02']/j2_count,
              jgene_count['TCRBJ02-03']/j2_count, jgene_count['TCRBJ02-04']/j2_count, 
              jgene_count['TCRBJ02-05']/j2_count, jgene_count['TCRBJ02-06']/j2_count,
              jgene_count['TCRBJ02-07']/j2_count,
              sep=',')

