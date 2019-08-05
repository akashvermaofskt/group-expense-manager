import React from 'react';
import {BrowserRouter as Router,Route,Link} from "react-router-dom";
import MainDash from "./MainDash";
import Profile from "./Profile";
import CreateGroup from "./CreateGroup";

class Dashboard extends React.Component{
    constructor(props){
        super(props);
        this.state={
        
        }
        this.logout=this.logout.bind(this);
    }

    logout(){
        this.props.logoutUser();
        
    }

    render(){
        return (
        <Router>
            <div className="container">
                <nav className="navbar sticky-top navbar-dark bg-dark " style={{color:'white'}}>
                    <a className="navbar-brand font-weight-bold" href="#">Group Expense Manager </a>
                    <div>
                        <span>Welcome [NAME] </span>
                        <Link to="/creategroup"><button className="btn btn-primary">Create group</button></Link>
                        <Link to="/" className="btn btn-light ml-3 md-1">Dashboard</Link>
                        <Link to="/profile" className="btn btn-light mr-3 ml-3 md-1">Profile</Link>
                        <Link to="/"><button className="btn btn-light mr-3 md-1" onClick={this.logout}>Logout</button></Link>
                    </div>
                </nav>

                <Route path="/" exact component={MainDash}/>
                <Route path="/profile" component={Profile}/>
                <Route path="/creategroup" component={CreateGroup}/>
            </div>
        </Router>
        
        );
    }
}

export default Dashboard;
