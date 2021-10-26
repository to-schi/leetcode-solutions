class DiningPhilosophers:
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        #The philosophers' ids are numbered from 0 to 4 in a clockwise order. Implement the function
        # void wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork) where:
        #     philosopher is the id of the philosopher who wants to eat.
        #     pickLeftFork and pickRightFork are functions you can call to pick the corresponding forks of that philosopher.
        #     eat is a function you can call to let the philosopher eat once he has picked both forks.
        #     putLeftFork and putRightFork are functions you can call to put down the corresponding forks of that philosopher.
        #     The philosophers are assumed to be thinking as long as they are not asking to eat (the function is not being called with their number).
        # Five threads, each representing a philosopher, will simultaneously use one object of your class to simulate the process. The function may be called for the same philosopher more than once, even before the last call ends.

# bis hier Vorgaben

fork1 = bool
fork2 = bool
fork3 = bool    
fork4 = bool
fork5 = bool

if fork1 and fork2 = True
    phil1_eat = True
if fork2 and fork3 = True
    phil2_eat = True
if fork3 and fork4 = True
    phil3_eat = True
if fork4 and fork5 = True   
    phil4_eat = True
if fork5 and fork1 = True
    phil5_eat = True

def main()
    fork1 = True
    fork2 = True
    fork3 = True
    fork4 = True

if fork1 and fork2 = True
    eat = True
else:
    eat = False
