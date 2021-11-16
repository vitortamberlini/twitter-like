document.addEventListener('DOMContentLoaded', () => {
    const infinite = new Waypoint.Infinite({
        element: document.querySelector('#feed'),
        offset: document.querySelector('footer'),
    });
})