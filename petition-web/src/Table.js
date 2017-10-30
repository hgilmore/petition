import React, { Component } from 'react';

import ReactTable from 'react-table';
import 'react-table/react-table.css';

class Table extends Component{

	constructor(props){
		super(props);

		// Set up an empty state to begin with as the method to get the data from
		// the API is asynchronous. When this renders for the first time there 
		// won't be anything other than the default state.
		this.state = {
			petition_id: props.match.params.id,
			rows: [],
			columns: [{
				Header: 'Name',
				accessor: 'name'
			}]
		};
	}

	componentWillMount(){
		this._getPetitionData();
	}

	_getPetitionData = () => {
		fetch('http://127.0.0.1:5000/petition/'+ this.state.petition_id)
		.then(response => {
			if (response.ok){
				return response;
			} else {
				let errorMessage =
					response.status(response.statusText),
					error = new Error(errorMessage);
					throw(error);
			}
		})
		.then(response => response.json())
		.then(json => {
			let _columns = [];

			// Get the headers out of the JSON
			// Convert to the required object
			for (let value of json.schema.fields) {
				_columns.push({Header: value.name, accessor: value.name});	
			}

			this.setState({ rows: json.data, columns: _columns })
			});
		}

	render(){

			const data = this.state.rows;
			const columns = this.state.columns;

			console.log(typeof(columns));

		return(

			<ReactTable data={data} columns={columns} />

			)
	}
}

export default Table;

/*
	Other things to do.

	- Percentage of UK population as a whole
	- Name of the petition on the screen
	- UI for picking a petition
*/