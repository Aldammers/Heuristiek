# Heuristiek
Authors:

- Stan Rozing
- Jan Marten
- Alexander Dammers 10528415

### Vereisten
Benodigden packages staan in de requirements.txt en zijn te downloaden via de command:

```
pip install -r requirements.txt
```
### Structure

Our algorithms and detials about them go into out algorithm folder: [Algorithms](/Code/Algorithms).

To find our research and results and conclusions check out our experimentation: [Results](/Results).

### Testing

To run the algorithms

```
python Main.py
```


        1. Start main: 'python main.py'
        2. Choose a protein
        3. Choose an algorithm to run





### Built With
 Python 3.6.5
 
 
## Algorithms

##### Be aware, to find out the time your computer needs to run these algorithms look up the runtime in [Results](/Results).

#### Random
It gets the best stability from a number of iterations of random position. The first two proteins, the ones with a relative small state space  the highest stabilities found with randomk are equal to those found with the Random Half and Breadth First (Piecewise) algorithm. For larger proteins, with larger states spaces they will not get the highest stabilities.

#### Random Halfs
Same as the random algorithm, but it wil cut the protein in 2 pieces. And then finds the best stability for the first piece in a given number of iterations. And then joins the second piece in a number of iterations to the first piece. 

#### Breadth First
An algorithm that starts at the root of the protein chain and explores the 3 directions it can build further. And it checks which direction is the best one, multiple are possible, and it goes further with those options. Because of exploring 3 directions for every amino acid it is very costly in the memory use. And can only be used with the first two protein chains.

#### Breadth first PieceWise
The Protein chain is chopped in pieces, which the size are hard coded into the algorithm and researched to be the most effective in getting the higgest stability. The way the protein get segmented is predecided based on common sense and empirical findings. First of all, unless it is the last, there cannot be a segment ending in a P since the last amino acid then would not be able to contribute to the score, so computing it inbetween would be a waste of time. Secondly, if the residu of best proteins after appending a segment gets larger, the next segment should be tiny, to reduce the running time and try to prevent the options from exploding. Furthermore, the average segment size is kept rather high to maintain more precision in finding the optimal solution.


        
 
