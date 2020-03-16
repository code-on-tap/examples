
import React from 'react'
import Violet from './violet'

class Blue extends React.Component {
  constructor( props ){
    super( props )

    this.handleViolet = this.handleViolet.bind( this )
  }

  componentDidMount(){
    this.element = document.getElementById( 'blue' )
    this.element.addEventListener( 'violet', this.handleViolet )
  }

  handleViolet( e ){
    //cancel the "white" event
    //if( e.cancelable )
    //  e.preventDefault()

    console.log( `'${e.currentTarget.id}' received the '${e.type}' event` )
  }

  render(){
    return (
      <ul id="blue" style={{ border: '2px solid blue', padding: '5px' }}>
        <li>A</li>
        <li>B</li>
        <li><Violet /></li>
        <li>D</li>
      </ul>
    )
  }
}

export default Blue
