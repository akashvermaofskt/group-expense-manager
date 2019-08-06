import React from 'react';
import {BrowserRouter as Router,Route,Link} from "react-router-dom";

class ActiveGroups extends React.Component{
    constructor(props){
        super(props);
        this.state={
        
        }
    }

    render(){
        return (
        <Router>
            <div className="container border">
                <div>
                    <h1 className="text-center  ">List of ActiveGroups</h1>
                </div>
                <div id="main" className="container-fluid mt-2" style={{background:"white",color:"black"}}>
                    <div className="d-flex flex-row align-items-center justify-content-start ">
                        
                        <div className="mt-5 md-5 " >

                        </div>
                    </div>
                </div>
            </div>
        </Router>
        
        );
    }
}

export default ActiveGroups;
