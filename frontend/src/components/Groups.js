import React from 'react';
import {BrowserRouter as Router,Route,Link} from "react-router-dom";
import ActiveGroups from "./ActiveGroups";
import SettledGroups from "./SettledGroups";
class Groups extends React.Component{
    constructor(props){
        super(props);
        this.state={
        
        }
    }

    render(){
        return (
        <Router>
            <div className="container border">
                <div id="main" className="container-fluid mt-2" style={{background:"white",color:"black"}}>
                    <div className="d-flex flex-column align-items-strech justify-content-start ">
                        <div className="mt-1 md-1 border" >
                            <ActiveGroups/>
                        </div>
                        <div className="mt-1 md-1 border" >
                            <SettledGroups/>
                        </div>
                    </div>
                </div>
            </div>
        </Router>
        
        );
    }
}

export default Groups;
