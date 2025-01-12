import axios from "axios";

const API_URL = "https://sgdx-dashboard.onrender.com";

export const fetchTimelineData = async (baseCcy, timeRange) => {
    try {
        const response = await axios.get(`${API_URL}/get/${baseCcy}/${timeRange}`, { withCredentials: false });
        return response.data; 
    } catch (error) {
        console.error("Error fetching data:", error);
    throw error; 
    }
};
