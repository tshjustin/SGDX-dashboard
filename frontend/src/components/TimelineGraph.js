import React, { useEffect, useState } from 'react';
import { 
    Box,
} from '@mui/material';
import { LineChart } from '@mui/x-charts/LineChart';

export default function TimelineGraph({ data }) {
    const [ccyPair, setCcyPair] = useState();
    const [xAxis, setXAxis] = useState([]);
    const [rates, setRates] = useState([]);

    useEffect(() => {
        if (data && Object.keys(data).length > 0) {
            console.log(data);

            const baseCcy = Object.keys(data)[0];
            const rateData = data[baseCcy];

            if (rateData) {
                const rates = Array.from(Object.values(rateData));
                const timestamps = Array.from(Object.keys(rateData));
                const formattedTimestamps = timestamps.map(timestamp => {
                    const date = new Date(timestamp);
                    return date.toLocaleString('en-GB', {
                        day: '2-digit',
                        month: 'short',
                        hour: '2-digit',
                        minute: '2-digit',
                    }).replace(',', '');
                });

                console.log("rates", rates);
                console.log("formattedTimestamps", formattedTimestamps);

                setCcyPair(baseCcy + "SGD");
                setRates(rates);
                setXAxis(formattedTimestamps);
            }
        }
    }, [data]);

    const tickLabelInterval = (value, index) => {
        return index % 2 === 0;  
    };

    if (xAxis.length === 0 || rates.length === 0 || !ccyPair) {
        return <div>Loading...</div>;
    }

    return (
        <Box sx={{ display: 'flex' }}>
            <LineChart
                width={1000}
                height={600}
                series={[
                    { data: rates, label: ccyPair },
                ]}
                xAxis={[
                    { 
                        scaleType: 'point', 
                        data: xAxis,
                        tick: {
                            interval: 'auto', // Use auto for handling overlapping
                            tickLabelInterval, // Custom function to control label visibility
                        },
                    }
                ]}
            /> 
        </Box>
    );
}