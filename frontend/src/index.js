import React from 'react';
import ReactDOM from 'react-dom/client';
import SideBar from './SideBar';
import TimelineGraph from './TimelineGraph';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
	<React.StrictMode>
		<SideBar />
		<TimelineGraph />
	</React.StrictMode>
);
