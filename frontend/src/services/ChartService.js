import api from "@/utils/api"

class ChartService {
  getAll(data) {
    return api.post(`/sales_chart`, JSON.stringify(data))
  }
}

export default new ChartService()