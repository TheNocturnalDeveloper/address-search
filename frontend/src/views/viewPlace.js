import React from 'react';

class ViewPlace extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            place: null
        };
    }

    render() {
        return <table>
            <tr><td>name</td><td></td></tr>
            <tr><td>class</td><td></td></tr>
            <tr><td>population</td><td></td></tr>
            <tr><td></td><td></td></tr>
        </table>
    }
}

export default ViewPlace;