import React from 'react'
import '../styles/NotificationStyle.css'

export default function NotificationComponent({props}) {
    return (
        <div className="notification" style={{right: props.right}}>
            <div className="container-a">
                <i onClick={() => props.xClicked(props.title)} className="fa fa-times icon"></i>
            </div>
            <div className="container-b">
                <p>{props.title}</p>
            </div>
        </div>
    )
}