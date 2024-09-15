<script setup>
import { FwbBreadcrumb, FwbBreadcrumbItem, FwbBadge } from 'flowbite-vue'
</script>

<template>
  <main>
     <div class="container mx-auto grid grid-cols-3">
      <div class="report mt-3">
          <fwb-breadcrumb solid>
            <fwb-breadcrumb-item home href="#">
              App
            </fwb-breadcrumb-item>
            <fwb-breadcrumb-item href="#">
              Reports
            </fwb-breadcrumb-item>
            <fwb-breadcrumb-item>
              <fwb-badge type="indigo">View</fwb-badge>
            </fwb-breadcrumb-item>
          </fwb-breadcrumb>
      </div>
     </div>

  </main>
</template>