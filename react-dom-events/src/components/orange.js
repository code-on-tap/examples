
import React from 'react'

import Yellow from './yellow'

class Orange extends React.Component {
  constructor( props ){
    super( props )

    this.handleViolet = this.handleViolet.bind( this )
    this.handleYellow = this.handleYellow.bind( this )
  }

  componentDidMount(){
    this.element = document.getElementById( 'orange' )
    this.element.addEventListener( 'violet', this.handleViolet )
    this.element.addEventListener( 'yellow', this.handleYellow )
  }

  handleViolet( e ){
    //cancel the "white" event
    //if( e.cancelable )
    //  e.preventDefault()

    console.log( `'${e.currentTarget.id}' received the '${e.type}' event` )
  }

  handleYellow( e ){
    //cancel the "white" event
    //if( e.cancelable )
    //  e.preventDefault()

    console.log( `'${e.currentTarget.id}' received the '${e.type}' event` )
  }

  render(){
    return (
      <div id="orange" style={{ border: '2px solid orange', padding: '5px' }}>
        <Yellow />
      </div>
    )
  }
}

export default Orange
