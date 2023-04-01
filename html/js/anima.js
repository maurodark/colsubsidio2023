import Letterize from "https://cdn.skypack.dev/pin/letterizejs@v2.0.0-GREsr0zVyFdrwnCAf2cJ/mode=imports/optimized/letterizejs.js";
const test = new Letterize({
        targets: ".animate-me"
      });

      const animation = anime.timeline({
        targets: test.listAll,
        delay: anime.stagger(100, {
          grid: [test.list[0].length, test.list.length],
          from: "center"
        }),
        loop: true
      });

      animation
        .add({
          scale: 0.5
        })
        .add({
          letterSpacing: "10px"
        })
        .add({
          scale: 1
        })
        .add({
          letterSpacing: "6px"
        });