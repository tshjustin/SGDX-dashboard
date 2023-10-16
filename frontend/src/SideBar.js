import React, { useState, useEffect } from 'react';
import { 
    Box,
    Drawer, 
    CssBaseline,
    Toolbar,
    Typography,
    Autocomplete,
    TextField
} from '@mui/material';

const drawerWidth = 300;
const options = ['EUR', 'JPY', 'MYR', 'THB', 'TWD', 'SGD'];

export default function SideBar({ setCcyPair }) {
    const [baseCcy, setBaseCcy] = useState("SGD");
    const [termCcy, setTermCcy] = useState("JPY");

    useEffect(() => {
        console.log(baseCcy + termCcy);
        setCcyPair(baseCcy + termCcy);
    }, [baseCcy, termCcy, setCcyPair]);

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
                    },
                }}
                variant="permanent"
                anchor="left"
            >
                <Toolbar>
                    <Typography variant="h5" noWrap component="div">
                        SGDX
                    </Typography>
                </Toolbar>
                <Box>
                    <Autocomplete
                        disableClearable
                        autoSelect
                        autoHighlight
                        blurOnSelect
                        autoComplete={false}
                        options={options}
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
                        options={options}
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
                </Box>
            </Drawer>
        </Box>
    );
}