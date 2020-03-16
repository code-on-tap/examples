# Examples
## 2020-03-16: DOM events in React
([code](https://github.com/code-on-tap/examples/tree/master/react-dom-events)|[zip](https://github.com/code-on-tap/examples/blob/master/react-dom-events/react-dom-events.zip))

### Discusion
React is still just HTML and JavaScript, so you're not locked into the JSX `key` and event attributes.  Following these simple steps, you can use the "old school" vanilla JS DOM events that have always existed.

1. Within your React component, add an `id` - or a very specific class/selector - to the element you're interested in; the trigger or listener.
```js
class Violet extends React.Component{
  //componentDidMount(){...}

  //handleClick(){...}

  render(){
    //bind handleClick to this
    return (
      <a id="violet" href="#violet" onClick={this.handleClick.bind(this)}>--violet--</a>
    )
  }
}
```

2. Implement the `componentDidMount()` function so you can find the element(s) after they render.
```js
class Violet extends React.Component{
  componentDidMount(){
    this.element = document.getElementById( 'violet' )
  }

  //handleClick(){...}

  //render(){...}
}
```

3. Use the element reference to trigger an event, or listen for one:
```js
class Violet extends React.Component{
  //componentDidMount(){...}

  handleClick(){
    //to stop bubbling, use e.stopPropagation()
    const myEvent = new Event( 'customEvent', { bubbles: true, cancelable: true })
    this.element.dispatchEvent( myEvent )
  }

  //render(){...}
}
```

4. The parents of this component can listen for the event as it bubbles up:

```js
class VioletParent extends React.Component{
  componentDidMount(){
    this.element = document.getElementById( 'violet-parent' )
    this.element.addEventListener( 'customEvent', e => {
      //Cancel bubble?
      //if( e.bubbles )
      //  e.stopPropagation()
      console.log( `violet-parent received ${e.type}` )
    })
  }

  render(){
    return (
      <div id="violet-parent">
        <Violet />
      </div>
    )
  }
}
```