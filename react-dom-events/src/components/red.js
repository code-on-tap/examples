
import React from 'react'

import Orange from './orange'

class Red extends React.Component {
  constructor( props ){
    super( props )

    this.handleViolet = this.handleViolet.bind( this )
    this.handleYellow = this.handleYellow.bind( this )
  }

  componentDidMount(){
    this.element = document.getElementById( 'red' )
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
      <div id="red" style={{ border: '2px solid red', padding: '5px' }}>
        <Orange />
      </div>
    )
  }
}

export default Red
