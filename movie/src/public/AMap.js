export default {
    MapLoader () {
        var script = document.createElement('script')
        script.type = 'text/javascript'
        script.async = true
        script.src =
            'http://webapi.amap.com/maps?v=1.4.11&callback=initAMap&key=a55652fb4e2c77556cd4f1234d849eaa'
        script.onerror = reject
        document.head.appendChild(script)
    }
}