import React from 'react'
import { NavLink } from 'react-router-dom'

export default function Header() {
  return (
    <div className='bg-green-600 py-2 font-bold px-3 text-white flex justify-between'>
      <p>Code Review System</p>
      <div>
        <NavLink to='/' ><span className='pr-5 font-thin'>Input</span></NavLink>
        <NavLink to='/output' ><span className='pr-5 font-thin'>Output</span></NavLink>
        
      </div>
    </div>
  )
}
