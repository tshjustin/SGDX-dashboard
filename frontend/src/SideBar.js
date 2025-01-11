import React, { useState, useEffect } from 'react';
import { 
    Box,
    Drawer, 
    CssBaseline,
    Typography,
    Autocomplete,
    TextField,
    Stack
} from '@mui/material';

const drawerWidth = 300;
const ccyOptions = ['EUR', 'JPY', 'MYR', 'THB', 'TWD', 'SGD'];
const timeRangeOptions = ['1', '7', '30', '60']

export default function SideBar({ setCcyPair }) {
    const [baseCcy, setBaseCcy] = useState("SGD");
    const [termCcy, setTermCcy] = useState("JPY");
    const [timeRange, setTimeRange] = useState(7)

    useEffect(() => {
        console.log(baseCcy + termCcy);
        console.log(timeRange);

        setCcyPair(baseCcy + termCcy);
        setTimeRange(timeRange)
    }, [baseCcy, termCcy, setCcyPair, timeRange]);

    const handleBaseCcyOnChange = (event) => {
        const prevSelectedCcy = baseCcy;

        if (event.type === "click") {
            const baseCcy = event.target.innerHTML;
            setBaseCcy(baseCcy);

            if (baseCcy === "SGD") {
                setTermCcy(prevSelectedCcy);
            } else {
                setTermCcy("SGD");
            } 
        } 
    }

    const handleTermCcyOnChange = (event) => {
        const prevSelectedCcy = termCcy;

        if (event.type === "click") {
            const termCcy = event.target.innerHTML;
            setTermCcy(termCcy);

            if (termCcy === "SGD") {
                setBaseCcy(prevSelectedCcy);
            } else {
                setBaseCcy("SGD");
            } 
        } 
    }

    const handleTimeRangeOnChange = (event) => {
        if (event.type === "click") {
            const timeRange = event.target.innerHTML;
            setTimeRange(timeRange);
        }   
    }

    return (
        <Box sx={{ display: 'flex' }}>
            <CssBaseline />
            <Drawer
                sx={{
                    width: drawerWidth,
                    flexShrink: 0,
                    '& .MuiDrawer-paper': {
                        width: drawerWidth,
                        boxSizing: 'border-box',
                        padding: '16px'
                    },
                }}
                variant="permanent"
                anchor="left"
                role="presentation"
            >
                <Typography variant="h5">
                    SGDX Dashboard
                </Typography>
                <Stack spacing={1}>
                    <Autocomplete
                        disableClearable
                        autoSelect
                        autoHighlight
                        blurOnSelect
                        autoComplete={false}
                        options={ccyOptions}
                        value={baseCcy}
                        onChange={handleBaseCcyOnChange}
                        renderInput={(params) => (
                            <TextField
                                {...params}
                                label="Base Currency"
                                variant="outlined"
                                size="medium"
                                margin="normal"
                            />
                        )}
                    />
                    <Autocomplete
                        disableClearable
                        autoSelect
                        autoHighlight
                        blurOnSelect
                        autoComplete={false}
                        options={ccyOptions}
                        value={termCcy}
                        onChange={handleTermCcyOnChange}
                        renderInput={(params) => (
                            <TextField
                                {...params}
                                label="Term Currency"
                                variant="outlined"
                                size="medium"
                                margin="normal"
                            />
                        )}
                    />
                    <Autocomplete 
                        disableClearable
                        autoSelect
                        autoHighlight
                        blurOnSelect
                        autoComplete={false}
                        options={timeRangeOptions}
                        value={timeRange}
                        onChange={handleTimeRangeOnChange}
                        renderInput={(params) => (
                            <TextField
                                {...params}
                                label="Time Range (days)"
                                variant="outlined"
                                size="medium"
                                margin="normal"
                            />
                        )}
                    />
                </Stack>
            </Drawer>
        </Box>
    );
}