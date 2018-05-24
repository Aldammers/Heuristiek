import RandomPiecewise as rp
import classes as c
import timeit


protein1 = c.Protein('HHPHHHPH')
protein2 = c.Protein('HHPHHHPHPHHHPH')
protein3 = c.Protein('HPHPPHHPHPPHPHHPPHPH')
protein4 = c.Protein('PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP')
protein5 = c.Protein('HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH')
protein6 = c.Protein('PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP')
protein7 = c.Protein('CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC')
protein8 = c.Protein('HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH')
protein9 = c.Protein('HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH')

proteins = [protein1, protein2, protein3, protein4, protein5, protein6, protein7, protein8, protein9]

n = input('How many times do you wish to fold all of the proteins? 10.000 times takes a couple of minutes f.y.i.: ')
n = int(n)

for i in range(len(proteins)):
    start = timeit.default_timer()
    protein = proteins[i]
    print('Protein', i + 1, 'gives a score of: ', end = '')
    startingpoint = [2*len(protein.sequence) + 3, 2*len(protein.sequence) + 3]
    protein.grit.reset()
    stepsize = protein.length // 2
    results = rp.RandomPiece_n(protein, n, startingpoint, stepsize)
    stop = timeit.default_timer()
    print(results[1])
    print ("Runtime: ", stop - start, "seconds")
    
    
    

