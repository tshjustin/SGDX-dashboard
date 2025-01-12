import React, { useState, useEffect } from 'react';
import SideBar from './components/SideBar';
import TimelineGraph from './components/TimelineGraph';
import { fetchTimelineData } from './services/api';

export default function App() {
    const [baseCcy, setBaseCcy] = useState('MYR');  
    const [timeRange, setTimeRange] = useState('1'); 
    const [timelineData, setTimelineData] = useState(null); 

    useEffect(() => {
        const getData = async () => {
          try {
            const data = await fetchTimelineData(baseCcy, timeRange);
            setTimelineData(data); 
          } catch (error) {
            console.error('Error fetching timeline data', error);
          }
        };
    
        getData();
    }, [baseCcy, timeRange]); 

    return (
        <>
            <SideBar
                baseCcy={baseCcy}
                setBaseCcy={setBaseCcy}
                timeRange={timeRange}
                setTimeRange={setTimeRange}
            />
            <TimelineGraph data={timelineData} />
        </>
    );
}