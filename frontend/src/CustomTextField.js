import React, { useState, useEffect } from 'react';
import { 
    Box,
    Autocomplete,
    TextField
} from '@mui/material';

const options = ['EUR', 'JPY', 'MYR', 'THB', 'TWD', 'SGD'];

export default function CustomTextField() {
    const [baseCcy, setBaseCcy] = useState("SGD");
    const [termCcy, setTermCcy] = useState("JPY");

    useEffect(() => {
        console.log(baseCcy + termCcy);
    }, [baseCcy, termCcy]);

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
    )
}