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

And choose which algorithm you want to use on which Protein





### Built With
 Python 3.6.5
 
 
## Algorithms

#### Random
It gets the best stability from a number of iterations of random position. The first two proteins, the ones with a relative small state space  the highest stabilities found with randomk are equal to those found with the Random Half and Breadth First (Piecewise) algorithm. For larger proteins, with larger states spaces they will not get the highest stabilities.

#### Random Halfs
Same as the random algorithm, but it wil cut the protein in 2 pieces. And then finds the best stability for the first piece in a given number of iterations. And then joins the second piece in a number of iterations to the first piece. 

#### Breadth First

#### Breadth first PieceWise

### How to use Breadth First Piecewise:

        1. Start main: 'python main.py'
        2. Choose an algorithm (1 to 9)
        3. Choose Piece Size, to get optimized result look at results table
        
 
