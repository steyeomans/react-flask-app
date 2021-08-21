import React, { Component } from 'react';

class TimeComponent extends Component {
  constructor(props){
    super(props);
    this.state = { time: Date.now() };
  }
  render(){
    return(
      <div> { this.state.time } </div>
    );
  }
  componentDidMount() {
    console.log("TimeComponent Mounted...")
  }
}
 
export default TimeComponent;