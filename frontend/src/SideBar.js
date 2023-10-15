import * as React from 'react';
import { 
    Box,
    Drawer, 
    CssBaseline,
    Toolbar,
    Typography
} from '@mui/material';
import CustomTextField from './CustomTextField';

const drawerWidth = 300;

export default function SideBar() {
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
                <CustomTextField />
            </Drawer>
        </Box>
    );
}