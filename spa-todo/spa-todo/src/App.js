import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import List from './List'
import Items from './Items'

class App extends Component {
    constructor() {
        super();
        this.state = {
            items: [],
            currentItem: {text:'', key:''},
        }
        this.inputElement = React.createRef();
    }
    handleInput = e => {
        const itemText = e.target.value
        const currentItem = { text: itemText, key: Date.now() }
        this.setState({
            currentItem,
        })
    }
    addItem = e => {
        e.preventDefault();
        const newItem = this.state.currentItem
        if (newItem.text !== '') {
            console.log(newItem)
            const items = [...this.state.items, newItem]
            this.setState({
                items: items,
                currentItem: { text: '', key: '' },
            })
        }
    }
    deleteItem = key => {
        const filteredItems = this.state.items.filter(item => {
            return item.key !== key
        })
        this.setState({
            items: filteredItems,
        })
    }
    render() {
        return (
        <div className="App">
            <Items entries={this.state.items} deleteItem={this.deleteItem} />
            <List
            addItem={this.addItem}
            inputElement={this.inputElement}
            handleInput={this.handleInput}
            currentItem={this.state.currentItem}
            />
        </div>
        );
    }
}

export default App;
