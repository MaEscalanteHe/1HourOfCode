import React, { Fragment } from 'react';

import Card from '../components/Card/Card';

const API = process.env.API;

class List extends React.Component {
	constructor() {
		super();
		this.state = {
			data: [],
			loading: true,
			searchTerm: '',
			error: '',
		};
	}

	async componentDidMount() {
		// const res = await fetch('../../assets/data.json');
		const res = await fetch(`${API}&s=batman`);
		const resJSON = await res.json();
		this.setState({ data: resJSON.Search, loading: false, error: '' });
	}

	async handleSumbit(e) {
		e.preventDefault();
		if (!this.state.searchTerm) {
			return this.setState({ error: 'Please write a valid text.' });
		}

		const res = await fetch(`${API}&s=${this.state.searchTerm}`);
		const data = await res.json();

		if (!data.Search) {
			return this.setState({ error: 'There are no resutls.' });
		}

		this.setState({ data: data.Search, error: '', searchTerm: '' });
	}

	render() {
		const { data, loading } = this.state;
		if (loading) {
			return <div>Loading...</div>;
		}

		return (
			<Fragment>
				<div className="row">
					<div className="col-md-4 offset-md-4 p-4">
						<form onSubmit={(e) => this.handleSumbit(e)}>
							<input
								type="text"
								className="form-control"
								placeholder="Search"
								onChange={(e) => this.setState({ searchTerm: e.target.value })}
								value={this.state.searchTerm}
								autoFocus
							/>
						</form>
						<p className="text-white">{this.state.error ? this.state.error : ''}</p>
					</div>
				</div>
				<div className="row">
					{data.map((movie, i) => {
						return <Card movie={movie} key={i} />;
					})}
				</div>
			</Fragment>
		);
	}
}

export default List;
