import React from 'react';
import {BrowserRouter as Router,Route,Link} from "react-router-dom";
import './Home.css';
import Login from './components/Login'
import Register from './components/Register';
import Dashboard from './components/Dashboard'
class Home extends React.Component{
  constructor(props){
    super(props);
    this.state={
      isLoggedIn:false
    }
    this.loginUser=this.loginUser.bind(this);
    this.logoutUser=this.logoutUser.bind(this);
  }

  loginUser(){
    this.setState({
      isLoggedIn:true
    });
  }

  logoutUser(){
    this.setState({
      isLoggedIn:false
    });
  }

  render(){

    if(this.state.isLoggedIn===true){
      return (
        <Dashboard logoutUser={this.logoutUser}/>
      );
    }

    return (
      <Router>
        <div className="container">
          <nav className="navbar sticky-top navbar-dark bg-dark " style={{color:'white'}}>
            <a className="navbar-brand font-weight-bold" href="#">Group Expense Manager </a>
            <div>
              <Link to="/" className="btn btn-light mr-3 ml-3 md-1">Login</Link>
              <Link to="/signup" className="btn btn-light mr-3 md-1">Signup</Link>
            </div>
          </nav>
          <div id="main" className="container-fluid mt-5" style={{background:"white",color:"black"}}>
            <div className="d-flex flex-column align-items-center justify-content-center ">
                <div>
                  <h1 className="font-weight-bold">Welcome people!</h1>
                </div>
                <div className="mt-5 md-5 " >
                  <Route
                    path='/'
                    render={(props) => <Login {...props} loginUser={this.loginUser} />}
                  />
                  <Route path="/signup" component={Register}/>
                </div>
            </div>
          </div>
        </div>
      </Router>
      
    );
  }
}

export default Home;
