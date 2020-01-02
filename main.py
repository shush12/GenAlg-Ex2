from random import randint

#Ex_2 in GenAlg's.
#The algorithm should find the best solution for
#this problem: fitness = (g0 + g1) - (g2 + g3) + (g4 + g5) - (g6 + g7)
#The most optimized solution is: 9,9,0,0,9,9,0,0
#(bigger fitness is better)

class Chromosome:
    def __init__(self):
        self.chromosome = [randint(0,9) for _ in range(8)] 
        self.fitness = 0
        
        #This function creates the chromosome.
    
    def fit(self):
        #This function will return the fitness of a chromosome.
        self.fitness = 0
        for i, gene in enumerate(self.chromosome):
            if i == 0 or i == 1 or i == 4 or i == 5:
                self.fitness += gene
            if i == 2 or i == 3 or i == 6 or i == 7:
                self.fitness -= gene
        
        return self.fitness
    
    def mutation(self, rate):
        #This function will mutate a chromosome.
        for i in range(len(self.chromosome)):
            random_num = randint(0,100)
            if random_num <= rate:
                #mutation code:
                self.chromosome[i] = randint(0,9)
        
        return self.chromosome



class Pupulation:
    def __init__(self, rate, termination_conition):
        self.poplist = []
        self.gennum = 1
        self.rate = rate
        self.sumfit_list = []
        self.termination_conition = termination_conition
        self.generation_list = []

    def population_creator(self, popsize,):
        for chrom in range(popsize):
            chrom = Chromosome()
            self.poplist.append(chrom)


    def pop_printing(self):
        fitsum = 0
        print("----------------------------------------")
        print("Generation:", self.gennum, "\n")
        for i, chrom in enumerate(self.poplist):
            print("#",i," ",chrom.chromosome,"\t",chrom.fit())
        for chromosome in self.poplist:
            fitsum += chromosome.fit()
        
        print("\n", "The Fitness sum is:", fitsum)
        print("----------------------------------------\n")
        self.gennum += 1


     
    
    def selection(self):
        fitness_list = []
        value = 0
        chance_list = []
        
        for chrom in self.poplist:
            fitness_list.append(chrom.fit())

        newfitness_list = list(map(plus36, fitness_list))
        for fitness in newfitness_list:
            for _ in range(fitness):
                chance_list.append(value)
            value += 1
        

        random_num1 = randint(0,len(chance_list)-1)
        random_num2 = randint(0,len(chance_list)-1)

        while random_num1 == random_num2:
            random_num2 = randint(0,len(chance_list)-1)


        value1 = chance_list[random_num1]
        value2 = chance_list[random_num2]




        parent1 = self.poplist[value1]
        parent2 = self.poplist[value2]
        

        return parent1, parent2
    
    
    def crossover(self):
        #I'm using 1 point crossover       
        parent1, parent2 = self.selection()
        
        cross_point = randint(0,7)
        
        child1 = Chromosome()
        child2 = Chromosome()

        child1.chromosome = parent1.chromosome[:cross_point]
        child1.chromosome.extend(parent2.chromosome[cross_point:])
        
        child2.chromosome = parent2.chromosome[:cross_point]
        child2.chromosome.extend(parent1.chromosome[cross_point:])


        #ADD MUTATION
        child1.chromosome = child1.mutation(self.rate)
        child2.chromosome = child2.mutation(self.rate)

        self.poplist.append(child1)
        self.poplist.append(child2)


        
    def kill_worse_chromosomes(self):
        fitness_list = []
        
        for i in range(len(self.poplist)):
            c_fitness = self.poplist[i]
            c_fitness = c_fitness.fit()
            fitness_list.append(c_fitness)

        for _ in range(2):
            item = sorted(fitness_list)[0]
            item_location = fitness_list.index(item)
            
            fitness_list.pop(item_location)
            self.poplist.pop(item_location)
            
    
    def stop_running(self):
        #This function will check if the population hasn't been
        #evolved for many generations, and if so it stops the code.
        

        self.generation_list.append(self.poplist)

        if self.termination_conition == 0:
            return False

        #------------------------------------------
        fitsum = 0
        for chromosome in self.poplist:
            fitsum += chromosome.fitness
        
        self.sumfit_list.append(fitsum)

        #------------------------------------------
        
        length = len(self.sumfit_list)

        if length > self.termination_conition:
            if self.sumfit_list[length - self.termination_conition - 1] >= self.sumfit_list[length - 1]:  
                return True
            else:
                return False
        
        else:
                return False
                
    
    
    # def print_best_population(self):
    #     c_num = 0
    #     fitsum = 0

    #     new_fit_list = sorted(self.sumfit_list)
    #     biggest_item = new_fit_list[len(new_fit_list) - 1]
    #     index = self.sumfit_list.index(biggest_item)
    #     gen = self.generation_list[index]

    #     print("  #", index, "\n")
        
    #     for chrom in gen:
    #         print("#", c_num, chrom.chromosome, chrom.fit())
    #         fitsum += chrom.fit()
    #         c_num += 1

    #     print("\n The total fitness of the population was:", fitsum)


def plus36(fitness):
    return fitness + 36


def main():
    mutation_rate = 20 # %.
    population_size = 10 #units in the population.
    termination_conition = 1 #Generation to terminate if the GA didn't evolve.(0 for don't stop.)
    

    termination = False
    pop1 = Pupulation(mutation_rate, termination_conition)
    pop1.population_creator(population_size)
    
    
    while termination == False:
        pop1.pop_printing()
        pop1.kill_worse_chromosomes()
        pop1.selection()
        pop1.crossover()   
        pop1.pop_printing()
        termination = pop1.stop_running()

if __name__ == "__main__":
    main()
