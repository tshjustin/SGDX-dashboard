import React from 'react';
import { 
    Box,
} from '@mui/material';
import { LineChart } from '@mui/x-charts/LineChart';
import exampleData from './exampleData.json';

export default function TimelineGraph({ data }) {

    const getRates = () => {
        const historicalData = exampleData.histoticalData;
        const ratesData = [];
        for (var data in historicalData) {
            const rate = historicalData[data].rate;
            ratesData.push(parseFloat(rate));
        }
        // console.log(ratesData);
        return ratesData; 
    }

    const getXAxis = () => {
        const historicalData = exampleData.histoticalData;
        const timeData = [];
        for (var data in historicalData) {
            const date = historicalData[data].queriedDate;
            const time = historicalData[data].queriedTime; 
            timeData.push(date + time);
        }
        // console.log(timeData)
        return timeData;
    }

    const getCcyPair = () => {
        const ccyPair = exampleData.currencyPair;
        return ccyPair;
    }

    return (
        <Box sx={{ display: 'flex' }}>
            <LineChart
                width={500}
                height={300}
                series={[
                    { data: getRates(), label: getCcyPair() },
                ]}
                xAxis={[
                    { scaleType: 'point', data: getXAxis() }
                ]}
            />
        </Box>
    );
}