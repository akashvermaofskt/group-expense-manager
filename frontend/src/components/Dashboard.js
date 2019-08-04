import React from 'react';
import {BrowserRouter as Router,Route,Link} from "react-router-dom";
import MainDash from "./MainDash"
import Profile from "./Profile"

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
                    <Link to="/" className="btn btn-light md-1">Dashboard</Link>
                    <Link to="/profile" className="btn btn-light mr-3 ml-3 md-1">Profile</Link>
                    <button className="btn btn-light mr-3 md-1" onClick={this.logout}>Logout</button>
                    </div>
                </nav>

                <Route path="/" exact component={MainDash}/>
                <Route path="/profile" component={Profile}/>
                
            </div>
        </Router>
        
        );
    }
}

export default Dashboard;
