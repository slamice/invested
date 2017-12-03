import React, {PropTypes} from 'react';
import {AppBar} from 'react-toolbox/lib/app_bar';
import {Layout, NavDrawer, Panel} from 'react-toolbox/lib/layout';
import theme from '../css/nav.css';

class App extends React.Component {
    state = {
        drawerActive: false,
        drawerPinned: false,
        sidebarPinned: false
    };

    toggleDrawerActive = () => {
        this.setState({
            drawerActive: !this.state.drawerActive
        });
    };

    toggleDrawerPinned = () => {
        this.setState({
            drawerPinned: !this.state.drawerPinned
        });
    }

    toggleSidebar = () => {
        this.setState({
            sidebarPinned: !this.state.sidebarPinned
        });
    };

    render() {
        return (
            <Layout>
                <NavDrawer active={this.state.drawerActive} pinned={this.state.drawerPinned} permanentAt='xxxl' onOverlayClick={this.toggleDrawerActive}>
                    <p>
                        Navigation, account switcher, etc. go here.
                    </p>
                </NavDrawer>
                <Panel>

                    <AppBar styleName="theme.AppBar" theme={theme} leftIcon='menu' onLeftIconClick={this.toggleDrawerActive}>
                    </AppBar>
                    <div style={{ flex: 1, overflowY: 'auto', padding: '1.8rem' }}>
                      <p>Some Text.</p>
                    </div>
                </Panel>
            </Layout>
        );
    }
}

// App.propTypes = {
//     children: PropTypes.node
// };

export default App;
