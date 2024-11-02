import { useEffect, useState } from 'react';

const GeneticAlgorithmComponent = () => {
    const [population, setPopulation] = useState([]);
    const [generation, setGeneration] = useState(0);

    // Simple genetic algorithm logic
    const runGeneticAlgorithm = () => {
        // Initialize population
        let pop = initializePopulation();
        let newPopulation = [];

        // Run for a specified number of generations
        for (let gen = 0; gen < 10; gen++) {
            pop.forEach(individual => {
                const fitness = calculateFitness(individual);
                if (fitness > 0.5) { // Arbitrary fitness threshold for demonstration
                    newPopulation.push(individual);
                }
            });
            pop = newPopulation; // Update population
            setGeneration(gen); // Update generation state
        }
        
        setPopulation(newPopulation);
    };

    // Function to initialize population
    const initializePopulation = () => {
        const size = 10; // Population size
        return Array.from({ length: size }, () => Math.round(Math.random())); // Random individuals
    };

    // Function to calculate fitness of an individual
    const calculateFitness = (individual) => {
        // Arbitrary fitness calculation
        return individual; // For binary individuals, fitness is simply the value
    };

    useEffect(() => {
        runGeneticAlgorithm();
    }, []);

    return (
        <div>
            <h1>Final Population (after {generation} generations)</h1>
            <pre>{JSON.stringify(population, null, 2)}</pre>
        </div>
    );
};

export default GeneticAlgorithmComponent;
