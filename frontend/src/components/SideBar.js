import React from 'react';
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
const ccyOptions = ['JPY', 'MYR', 'THB'];
const timeRangeOptions = ['1', '7', '30', '60']

export default function SideBar({ baseCcy, setBaseCcy, timeRange, setTimeRange }) {
    const handleBaseCcyChange = (event) => {
        if (event.type === "click") {
            setBaseCcy(event.target.innerHTML);
        } 
    }

    const handleTimeRangeChange = (event) => {
        if (event.type === "click") {
            setTimeRange(event.target.innerHTML);
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
                        onChange={handleBaseCcyChange}
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
                        options={timeRangeOptions}
                        value={timeRange}
                        onChange={handleTimeRangeChange}
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