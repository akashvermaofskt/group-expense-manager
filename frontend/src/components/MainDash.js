import React from 'react';
import {BrowserRouter as Router,Route,Link} from "react-router-dom";
import Groups from "./Groups";
import ShortProfile from "./ShortProfile";
import Friends from "./Friends";
class MainDash extends React.Component{
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
                    <h1 className="text-center font-weight-bold">Welcome to your Dashboard!</h1>
                </div>
                <div id="main" className="container-fluid mt-5 border" style={{background:"white",color:"black"}}>
                    <div className="d-flex flex-row align-items-start justify-content-center ">
                        <div className="mt-5 md-5 " >
                            <ShortProfile/>
                        </div>
                        <div className="mt-5 md-5 " >
                            <Groups/>
                        </div>
                        <div className="mt-5 md-5 " >
                            <Friends/>
                        </div>
                    </div>
                </div>
            </div>
        </Router>
        
        );
    }
}

export default MainDash;
