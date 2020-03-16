
import React from 'react'

class Violet extends React.Component {
  constructor( props ){
    super( props )

    this.handleClick = this.handleClick.bind( this )
  }

  componentDidMount(){
    this.element = document.getElementById( 'violet' )
  }

  handleClick( e ){
    //cancel the click event
    if( e.cancelable )
      e.preventDefault()

  
    //trigger a "violet" event to bubble up
    const violetEvent = new Event( 'violet', { bubbles: true, cancelable: true })
    this.element.dispatchEvent( violetEvent )
  }

  render(){
    return (
      <a id="violet" href="#violet" onClick={this.handleClick}>--violet--</a>
    )
  }
}

export default Violet
