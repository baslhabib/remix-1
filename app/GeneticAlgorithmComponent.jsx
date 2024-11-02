import { useEffect, useState } from 'react';

const GeneticAlgorithmComponent = () => {
    const [population, setPopulation] = useState([]);

    const runAlgorithm = async () => {
        try {
            const response = await fetch('https://your-flask-service-url.onrender.com/run-genetic-algorithm'); // Update this URL
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            console.log("Data received from server:", data); // For debugging
            setPopulation(data.best_individual);  // Assuming this is the expected data structure
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    };

    useEffect(() => {
        runAlgorithm();
    }, []);

    return (
        <div>
            <h1>Final Population</h1>
            <pre>{JSON.stringify(population, null, 2)}</pre>
        </div>
    );
};

export default GeneticAlgorithmComponent;
