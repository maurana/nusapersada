<script setup>
import { ref } from 'vue'
import { FwbAvatar } from 'flowbite-vue'
import { RouterLink } from 'vue-router'
import { createPopper } from '@popperjs/core'

const _dS = ref(false)
const _mS = ref(false)

function toggleDropdown() { this._dS?this._dS=false:this._dS=true }
function toggleMenu() {
  if(this._mS){
    this._mS = false
  } else {
    this._mS = true
    const menubutton = document.querySelector('#menu-button')
    const menutooltip = document.querySelector('#navbar-user')
    createPopper(menubutton, menutooltip, {
      placement: "bottom-start"
    })
  }
}
</script>

<template #default>
<nav class="bg-white border-gray-200 dark:bg-gray-900">
  <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
    <div class="flex items-center space-x-3 rtl:space-x-reverse">
      <a href="#" class="">
        <img src="/logo.svg" class="h-8" alt="Logo" />
      </a>

      <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1">
        <ul class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-white md:space-x-3 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
          <li>
            <RouterLink to="/" class="block font-bold py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Sales</RouterLink>
          </li>
          <li>
            <RouterLink to="/report" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Report</RouterLink>
          </li>
        </ul>
      </div>
    </div>

    <div class="flex items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
      <button class="flex items-center font-medium text-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-700" fill="none" viewBox="0 0 23 23" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /></svg>
        <div class="absolute inline-flex items-center justify-center w-3 h-3 text-xs font-bold text-white bg-blue-800 border-2 border-white rounded-full -top-2 -end-2 dark:border-gray-900"></div>
      </button>
      <button type="button" class="flex items-center text-sm bg-white rounded-full md:me-0" id="user-menu-button" aria-expanded="false" data-dropdown-toggle="user-dropdown" data-dropdown-placement="bottom" @click="toggleDropdown()">
        <div class="flex justify-center items-center space-x-2">
            <p class="font-normal">Maulana</p>
            <fwb-avatar bordered img="https://avatars.githubusercontent.com/u/45948023?v=4" rounded status="online" />
            <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 transform transition-transform duration-200 ease-in-out" :class="_dS ? 'rotate-180' : 'rotate-0'"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
        </div>
    </button>
      <!-- Dropdown menu -->
      <div class="z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600" id="user-dropdown">
        <div class="px-4 py-3">
          <span class="block text-sm text-gray-900 dark:text-white"><a href="#" class="text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">
              <div class="inline-flex items-center">
                <svg class="w-4 h-4 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Zm0 0a8.949 8.949 0 0 0 4.951-1.488A3.987 3.987 0 0 0 13 16h-2a3.987 3.987 0 0 0-3.951 3.512A8.948 8.948 0 0 0 12 21Zm3-11a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                </svg> &nbsp;Your Profile
              </div>
            </a></span>
          <span class="block text-sm  text-gray-500 truncate dark:text-gray-400">admin@email.com</span>
        </div>
        <ul class="py-2" aria-labelledby="user-menu-button">
          <li>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">
              <div class="inline-flex items-center">
                <svg class="w-4 h-4 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.933 13.909A4.357 4.357 0 0 1 3 12c0-1 4-6 9-6m7.6 3.8A5.068 5.068 0 0 1 21 12c0 1-3 6-9 6-.314 0-.62-.014-.918-.04M5 19 19 5m-4 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                </svg> &nbsp;Change password
              </div>
            </a>
          </li>
          <li>
            <a href="#" class="font-bold block px-4 py-2 text-sm text-red-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">
              <div class="inline-flex items-center">
                <svg class="w-4 h-4 text-red-700 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H8m12 0-4 4m4-4-4-4M9 4H7a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h2"/>
                </svg> &nbsp;Sign out
              </div>
            </a>
          </li>
        </ul>
      </div>
      <!-- button toggle nav -->
      <button @click="toggleMenu()" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-expanded="false" id="menu-button">
        <span class="sr-only">Open main menu</span>
        <svg fill="currentColor" viewBox="0 0 20 20" class="w-5 h-5"><path v-show="!_mS" fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM9 15a1 1 0 011-1h6a1 1 0 110 2h-6a1 1 0 01-1-1z" clip-rule="evenodd"></path><path v-show="_mS" fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"clip-rule="evenodd"></path>
        </svg>
     </button>
  </div>
  <div v-show="_mS" class="z-30 items-center justify-between w-full md:hidden md:w-auto md:order-1" id="navbar-user">
        <ul class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-white md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
            <li>
            <RouterLink to="/" class="font-bold block py-2 px-1">Sales</RouterLink>
            </li>
            <li>
            <RouterLink to="/report" class="block py-2 px-1">Report</RouterLink>
            </li>
        </ul>
  </div>
  </div>
</nav>
</template>