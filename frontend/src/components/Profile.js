import React from 'react';
import {BrowserRouter as Router,Route,Link} from "react-router-dom";

class Profile extends React.Component{
    constructor(props){
        super(props);
        this.state={
        
        }
    }

    render(){
        return (
        <Router>
            <div className="container">
                <div>
                    <h1 className="text-center font-weight-bold">Welcome to your Profile!</h1>
                </div>
                <div id="main" className="container-fluid mt-5" style={{background:"white",color:"black"}}>
                    <div className="d-flex flex-row align-items-center justify-content-center ">
                        
                        <div className="mt-5 md-5 " >

                        </div>
                    </div>
                </div>
            </div>
        </Router>
        
        );
    }
}

export default Profile;
