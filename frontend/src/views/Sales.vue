<script>
import { initFlowbite } from 'flowbite'
import { saleschart } from '@/utils/chart'
import SalesService from '@/services/SalesService'
import ChartService from '@/services/ChartService'
import PopularService from '@/services/PopularService'

export default {
  name: "Sales",
  data() {
    return {
      dt_sales: [],
      dt_popular: [],
      chart: {},
      amount: 0,
      percentage: 0,
      page: 1,
      total_data: 0,
      total_page: 0,
      has_next: false,
      has_previous: false,
      links: {
        start: 0,
        next: 0
      },
      parameters: {
        params: [
          {
            keyword: "",
            data_periode_start: "",
            data_periode_end: "",
            total_data_show: 10
          }
        ]
      }
    }
  },
  methods: {
    viewChart() {
      const params = {
        "params": [{
          "keyword": "",
          "dates":[
            {"date":"2024-09-08"},
            {"date":"2024-09-09"},
            {"date":"2024-09-10"},
            {"date":"2024-09-11"},
            {"date":"2024-09-12"}
          ] 
        }]
      }

      ChartService.getAll(params)
        .then(res => {
          let all_data_chart = [
              {
                name: "Sales",
                data: res.data.sales,
                color: "#E3A008",
              },
              {
                name: "Items",
                data: res.data.items,
                color: "#7E3BF2",
              },
              // {
              //   name: "Prices",
              //   data: res.data.prices,
              //   color: "#DB2777",
              // },
          ]
          this.amount = res.data.amount
          this.percentage = res.data.percentage
          this.chart = saleschart(res.data.categories, all_data_chart)
        })
        .catch(e => console.log(e))
    },
    salesList() {
      SalesService.getAll(this.parameters, this.page)
        .then(res => {
          this.dt_sales = res.data.data[0].rows;
          this.page = res.data.data[0].Page
          this.total_data = res.data.data[0].total_data
          this.total_page = res.data.data[0].total_page
          this.links.start = res.data.data[0].links.start
          this.links.next = res.data.data[0].links.next
          this.has_previous = res.data.data[0].has_previous
          this.has_next = res.data.data[0].has_next
        })
        .catch(e => {
          console.log(e)
        })
    },
    productpopularList() {
      this.parameters.params[0].total_data_show = 5
      this.parameters.params[0].data_periode_start = "08/09/2024"
      this.parameters.params[0].data_periode_end = "12/09/2024"
      PopularService.getAll(this.parameters)
        .then(res => {
          this.dt_popular = res.data.data
          this.resetParams()
        })
        .catch(e => {
          console.log(e)
        })
    },
    resetParams() {
      this.parameters.params[0].total_data_show = 10
      this.parameters.params[0].data_periode_start = ""
      this.parameters.params[0].data_periode_end = ""
    },
    handlePagination(index, type, total) {
      this.page = index
      if (this.page >=1) {
        if (type === 'next' && this.has_next == true) this.page = index+1
        if (type === 'previous' && this.has_previous == true) this.page = index-1
        this.salesList()
      }
      
    },
    handleRows(rows) {
      this.parameters.params[0].total_data_show = rows
      this.salesList()
    },
    handleSearch(value) {
      this.parameters.params[0].keyword = value
      this.salesList()
    },
    // handleValueStartDate(value) {
    //   val = document.getElementById("datepicker-range-start").value 
    //   console.log(val)
    //   this.parameters.params[0].data_periode_start = value
    // },
    // handleValueEndDate(value) {
    //   console.log(value)
    //   this.parameters.params[0].data_periode_end = value
    // },
    // handleDateRange() {
    //   console.log(this.parameters.params[0].data_periode_start)
    //   console.log(this.parameters.params[0].data_periode_end)
    // }
  },
  mounted() {
    initFlowbite()
    this.salesList()
    this.viewChart()
    this.productpopularList()
  }
}
</script>

<template>
  <main>
      <div class="max-w-screen-xl relative w-full container mx-auto md:grid md:grid-cols-12">
      <div class="report w-full mt-3 md:flex md:flex-row md:flex-wrap gap-3">
        <div class="md:flex-col md:flex-wrap md:basis-5/12">
          <div class="max-w-xl w-full md:justify-center md:item-center bg-white rounded-lg shadow dark:bg-gray-800">
          <div class="flex justify-between p-4 md:p-6 pb-0 md:pb-0">
            <div>
              <h5 class="leading-none text-2xl font-bold text-gray-900 dark:text-white pb-2">Rp {{ amount.toFixed(3) }}</h5>
              <p class="text-base font-normal text-gray-500 dark:text-gray-400">Sales this week</p>
            </div>
            <div
              class="flex items-center px-2.5 py-0.5 text-base font-semibold text-pink-600 dark:text-pink-500 text-center">
              {{ percentage.toFixed() }}%
              <svg class="w-3 h-3 ms-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 14">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13V1m0 0L1 5m4-4 4 4"/>
              </svg>
            </div>
          </div>
          <apexchart class="px-2.5 max-w-xl w-full" type="area" :options="chart" :series="chart.series" />
          </div>   
          <div class="w-full bg-white rounded-lg shadow dark:bg-gray-800 mt-3 mb-3 p-3">
            <div class="relative overflow-x-auto md:overflow-hidden">
                <div class="flex items-center py-0.5 text-base font-semibold text-gray-800 mb-3 mt-2">Products Popular</div>
                <table class="text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mt-3 mb-3">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="p-2">
                                No
                            </th>
                            <th scope="col" class="px-2 py-2">
                              <div class="flex items-center">
                              Name
                              </div>
                            </th>
                            <th scope="col" class="px-2 py-2">
                              <div class="flex items-center">
                              Price
                              </div>
                            </th>
                            <th scope="col" class="px-2 py-2">
                              <div class="flex items-center">
                              Total QTY
                              </div>
                            </th>
                            <th scope="col" class="px-2 py-2">
                              <div class="flex items-center">
                              Total Price
                              </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(val, index) in dt_popular" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-2 p-2 font-semibold">{{ index+1 }}</td>
                        <td class="px-2 py-2">{{ val.products_name }}</td>
                        <td class="px-2 py-2">{{ val.products_price }}</td>
                        <td class="px-2 py-2">{{ val.total_qty }}</td>
                        <td class="px-2 py-2">{{ val.total_price.toFixed(2) }}</td>
                      </tr>
                    </tbody>
                </table>
            </div>
          </div>
        </div>
        <div class="w-full-md basis-6/12">
          <div class="bg-white shadow rounded-lg bg-clip-border p-6 mb-3">
            <div class="relative overflow-x-auto">
                <div class="flex items-center py-0.5 text-base font-semibold text-gray-800 mb-3">History Transaction</div>
                  <div class="justify-between md:flex md:items-center space-y-4 md:space-y-0 pb-4 bg-white">
                    <div class="inline-flex md:flex-row-reverse" >
                      <div class="relative">
                        <div class="absolute inset-y-0 inset-x-0 start-0 flex mt-3 ps-3 pointer-events-none ml-3 sm:items-center">
                            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                            </svg>
                        </div>
                        <input :value="parameters.params[0].keyword" @input="event => handleSearch(event.target.value)" type="text" id="table-search-users" class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50" placeholder="">
                      </div>
                      <div class="ml-2">
                        <button id="rowsActionButton" data-dropdown-toggle="rowsAction" class="inline-flex items-center text-gray-500 bg-white border border-gray-300 font-medium rounded-lg text-sm px-3 py-2" type="button">
                            <span class="sr-only">Action button</span>
                            Rows - {{ parameters.params[0].total_data_show }}
                            <svg class="ml-1 w-2.5 h-2.5 ms-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                            </svg>
                        </button>
                        <!-- Dropdown menu -->
                        <div id="rowsAction" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600">
                            <ul class="py-1 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="rowsActionButton">
                                <li>
                                    <button @click="handleRows(10)" class="block w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">10</button>
                                </li>
                                <li>
                                    <button @click="handleRows(25)" class="block w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">25</button>
                                </li>
                                <li>
                                    <button @click="handleRows(50)" class="block w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">50</button>
                                </li>
                                <li>
                                    <button @click="handleRows(100)" class="block w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">100</button>
                                </li>
                            </ul>
                            <div class="py-1">
                                <button @click="handleRows(total_data)" class="block w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">All Data</button>
                            </div>
                        </div>
                      </div>
                      <!-- <div class="ml-2">
                        <button id="daterangeActionButton" data-dropdown-toggle="daterangeAction" data-dropdown-ignore-click-outside-class="datepicker" class="inline-flex items-center text-gray-500 bg-white border border-gray-300 font-medium rounded-lg text-sm px-3 py-2" type="button">
                            <span class="sr-only">Action button</span>
                            Date
                            <svg class="ml-1 w-2.5 h-2.5 ms-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                            </svg>
                        </button>
                        <div id="daterangeAction" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600 p-2">
                            <div id="date-range-picker" date-rangepicker class="flex items-center gap-2">
                                <div class="relative group">
                                <input id="datepicker-range-start" type="text" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="Select date start" :value="parameters.params[0].data_periode_start" @input="handleValueStartDate($event.target.value)">
                                </div>
                                <span class="text-gray-500">to</span>
                                <div class="relative group">
                                <input id="datepicker-range-end" type="text" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="Select date end" :value="parameters.params[0].data_periode_end" @input="handleValueEndDate(event.target.value)">
                                </div>
                                <span class="text-gray-500"><button @click="handleDateRange()" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button></span>
                            </div>
                        </div>
                      </div> -->
                    </div>
                    <div class="relative">
                      <button type="button" class="text-gray-900 bg-gradient-to-r from-teal-200 to-lime-200 hover:bg-gradient-to-l hover:from-teal-200 hover:to-lime-200 focus:ring-4 focus:outline-none focus:ring-lime-200 dark:focus:ring-teal-700 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 mt-2 btn-block" >Create Data</button>
                    </div>
                </div>
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mt-3">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="px-4 py-4">
                              <div class="flex items-center">
                                No&nbsp;
                                <svg class="w-3 h-3 ms-1.5" aria-hidden="true" fill="currentColor" viewBox="0 0 24 24">
                              <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                              </svg>
                              </div>
                            </th>
                            <th scope="col" class="px-4 py-4">
                              <div class="flex items-center">
                              Transaction Code&nbsp;
                              <svg class="w-3 h-3 ms-1.5" aria-hidden="true" fill="currentColor" viewBox="0 0 24 24">
                              <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                              </svg>
                              </div>
                            </th>
                            <th scope="col" class="px-4 py-4">
                              <div class="flex items-center">
                              Customers&nbsp;
                              <svg class="w-3 h-3 ms-1.5" aria-hidden="true" fill="currentColor" viewBox="0 0 24 24">
                              <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                              </svg>
                              </div>
                            </th>
                            <th scope="col" class="px-4 py-4">
                              <div class="flex items-center">
                              Total Item&nbsp;
                              <svg class="w-3 h-3 ms-1.5" aria-hidden="true" fill="currentColor" viewBox="0 0 24 24">
                              <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                              </svg>
                              </div>
                            </th>
                            <th scope="col" class="px-4 py-4">
                              <div class="flex items-center">
                              Total Price&nbsp;
                              <svg class="w-3 h-3 ms-1.5" aria-hidden="true" fill="currentColor" viewBox="0 0 24 24">
                              <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                              </svg>
                              </div>
                            </th>
                            <th scope="col" class="px-4 py-4">
                              <div class="flex items-center">
                              Sales Date&nbsp;
                              <svg class="w-3 h-3 ms-1.5" aria-hidden="true" fill="currentColor" viewBox="0 0 24 24">
                              <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                              </svg>
                              </div>
                            </th>
                            <th scope="col" class="px-4 py-4">
                                Action
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(val, index) in dt_sales" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                            <td class="px-4 py-4 font-semibold">{{ index+1 }}</td>
                            <td class="px-4 py-4">{{ val.sales_code }}</td>
                            <td class="px-4 py-4">{{ val.customers_name }}</td>
                            <td class="px-4 py-4">{{ val.sale_items_total }}</td>
                            <td class="px-4 py-4">{{ val.sale_price_total.toFixed(2) }}</td>
                            <td class="px-4 py-4">{{ val.sales_date }}</td>
                            <td class="px-4 py-4">
                                <div class="inline">
                                  <button type="button" data-tooltip-target="tooltip-verify">
                                    <svg class="w-5 h-5 text-green-600" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                                    <path fill-rule="evenodd" d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm13.707-1.293a1 1 0 0 0-1.414-1.414L11 12.586l-1.793-1.793a1 1 0 0 0-1.414 1.414l2.5 2.5a1 1 0 0 0 1.414 0l4-4Z" clip-rule="evenodd"/>
                                    </svg>
                                  </button>
                                  <div id="tooltip-verify" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-700 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">Verify<div class="tooltip-arrow" data-popper-arrow></div>
                                  </div>
                                  <button type="button" data-tooltip-target="tooltip-edit">
                                    <svg class="w-5 h-5 text-blue-600" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                                    <path fill-rule="evenodd" d="M11.32 6.176H5c-1.105 0-2 .949-2 2.118v10.588C3 20.052 3.895 21 5 21h11c1.105 0 2-.948 2-2.118v-7.75l-3.914 4.144A2.46 2.46 0 0 1 12.81 16l-2.681.568c-1.75.37-3.292-1.263-2.942-3.115l.536-2.839c.097-.512.335-.983.684-1.352l2.914-3.086Z" clip-rule="evenodd"/>
                                    <path fill-rule="evenodd" d="M19.846 4.318a2.148 2.148 0 0 0-.437-.692 2.014 2.014 0 0 0-.654-.463 1.92 1.92 0 0 0-1.544 0 2.014 2.014 0 0 0-.654.463l-.546.578 2.852 3.02.546-.579a2.14 2.14 0 0 0 .437-.692 2.244 2.244 0 0 0 0-1.635ZM17.45 8.721 14.597 5.7 9.82 10.76a.54.54 0 0 0-.137.27l-.536 2.84c-.07.37.239.696.588.622l2.682-.567a.492.492 0 0 0 .255-.145l4.778-5.06Z" clip-rule="evenodd"/>
                                    </svg>
                                  </button>
                                  <div id="tooltip-edit" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-700 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">Edit<div class="tooltip-arrow" data-popper-arrow></div>
                                  </div>
                                  <button type="button" data-tooltip-target="tooltip-delete" data-modal-target="modal-delete" data-modal-toggle="modal-delete">
                                    <svg class="w-5 h-5 text-red-600" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                                    <path fill-rule="evenodd" d="M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z" clip-rule="evenodd"/>
                                    </svg>
                                  </button>
                                  <div id="tooltip-delete" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-700 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">Delete<div class="tooltip-arrow" data-popper-arrow></div>
                                  </div>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <nav class="flex items-center flex-column flex-wrap md:flex-row justify-between pt-4 mb-3" aria-label="Table navigation">
                    <span class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-4 md:mb-0 block w-full md:inline md:w-auto">Showing <span class="font-semibold text-gray-900 dark:text-white">{{ links.start }}-{{ links.next }}</span> of <span class="font-semibold text-gray-900 dark:text-white">{{ total_data }}</span></span>
                    <ul class="inline-flex -space-x-px rtl:space-x-reverse text-sm h-8">
                        <li>
                            <button @click="handlePagination(page,'previous',total_page)" class="flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Previous</button>
                        </li>
                        <li v-for="(val, index) in total_page" :key="index" class="text-gray-600">
                            <button @click="handlePagination(index+1, '',total_page)" :class="{ 'text-blue-600 bg-blue-50': index+1 == page }" class="flex items-center justify-center px-3 h-8 border border-gray-300 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">{{ index+1 }}</button>
                        </li>
                        <li>
                            <button @click="handlePagination(page, 'next',total_page)" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Next</button>
                        </li>
                    </ul>
                </nav>
            </div>
          </div>
          <!-- <div id="modal-delete" data-modal-placement="top-right" tabindex="-1" class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
            <div class="relative p-4 w-full max-w-md max-h-full">
                <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                    <button type="button" class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="modal-delete">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                    <div class="p-4 md:p-5 text-center">
                        <svg class="mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
                        </svg>
                        <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">Are you sure you want to delete sales?</h3>
                        <button data-modal-hide="modal-delete" type="button" class="text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center">
                            Yes, Delete !
                        </button>
                        <button data-modal-hide="modal-delete" type="button" class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">No, cancel</button>
                    </div>
                </div>
            </div>
          </div> -->
        </div>
      </div>
      <footer class="">
          <div class="mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8">
            <hr class="mb-6 border-gray-200 mx-auto dark:border-gray-700" />
            <div class="flex items-center justify-between">
                <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2024 <a href="https://thisismaulana.vercel.app/" class="hover:underline">Maulana™</a>. All Rights Reserved.
                </span>
                <div class="flex sm:justify-center">
                  <span class="text-sm text-green-500 sm:text-center dark:text-gray-400">
                    Software v1.0.0
                  </span>
                </div>
            </div>
          </div>
      </footer>
     </div>
  </main>
</template>