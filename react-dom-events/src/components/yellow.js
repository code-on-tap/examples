
import React from 'react'

import Blue from './blue'

class Yellow extends React.Component{
  constructor( props ){
    super( props )

    this.handleViolet = this.handleViolet.bind( this )
  }

  componentDidMount(){
    this.element = document.getElementById( 'yellow' )
    this.element.addEventListener( 'violet', this.handleViolet )

    document.getElementById( 'green' ).addEventListener( 'violet', this.handleViolet )
  }

  handleViolet( e ){
    console.log( `'${e.currentTarget.id}' received the '${e.type}' event` )

    if( e.currentTarget.id === 'yellow' ){
      if( e.bubbles ){
        e.stopPropagation()
        console.log( `'${e.currentTarget.id}' cancelled the '${e.type}' event from bubbling` )
      }

      //trigger a blue event
      const yellowEvent = new Event( 'yellow', { bubbles: true, cancelable: true })
      e.currentTarget.dispatchEvent( yellowEvent )

      //just in case
      return false
    }
  }

  render(){
    return (
      <table id="yellow" style={{ border: '2px solid yellow', padding: '5px' }}>
      <tbody>
      <tr>
      <td>col1</td>
      <td id="green" style={{ border: '2px solid green', padding: '5px' }}>

        <Blue />

      </td>
      <td>col3</td>
      </tr>
      </tbody>
      </table>
    )
  }
}

export default Yellow
