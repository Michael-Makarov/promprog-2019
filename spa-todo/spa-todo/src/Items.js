import React, { Component } from 'react'

class Items extends Component {
  createTasks = item => {
    return (
        <li
            key={item.key}
            onClick={() => this.props.deleteItem(item.key)}>
        {item.text}
        </li>
    )
  }
  render() {
    const entries = this.props.entries
    const listItems = entries.map(this.createTasks)

    return <ul className="theList">{listItems}</ul>
  }
}

export default Items 
