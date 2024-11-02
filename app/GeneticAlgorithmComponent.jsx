import { useEffect, useState } from 'react';

const GeneticAlgorithmComponent = () => {
    const [population, setPopulation] = useState([]);

    const runAlgorithm = async () => {
        const response = await fetch('/run-genetic-algorithm');
        const data = await response.json();
        setPopulation(data);
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
