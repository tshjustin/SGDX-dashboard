import React, { useState, useEffect } from 'react';
import SideBar from './SideBar';
import TimelineGraph from './TimelineGraph';

export default function App() {
    const [ccyPair, setCcyPair] = useState("");
    const [data, setData] = useState({});

    // Every time the ccyPair changes, 
    // send a request to the backend to retieve the rates for that ccyPair
    useEffect(() => {
        fetch("http://localhost:9000") // sample backend endpoint
        .then(response => response.json())
        .then(data => setData(data))
    }, [ccyPair]);

    return (
        <>
            <SideBar setCcyPair={setCcyPair}/>
		    <TimelineGraph data={data}/>
        </>
    );
}