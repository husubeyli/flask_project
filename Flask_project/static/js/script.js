$(document).ready(function () {
  let randCount = 0;
  let arrayCount = 0;
  let products = [
    {
      title: "İncognito (beyinin gizli həyatı)",
      thumbnail: "../static/images/Inkognito.png",
      body: "",
      writer: "David Eagleman",
      old_price: 15,
      new_price: 12,
      count: 2,
      status: "delete",
      category: "psixologiya",
    },
    {
      title: "Səfillər",
      thumbnail: "../static/images/sefiller.jpg",
      body: "",
      writer: "Victor Hugo",
      old_price: 32,
      new_price: 13,
      count: 3,
      status: "active",
      category: "roman",
    },
    {
      title: "1984",
      thumbnail: "../static/images/1984.jpg",
      body: "",
      writer: "George Orwell",
      old_price: 12,
      new_price: 21,
      count: 3,
      status: "active",
      category: "bilim-kurgu",
    },
    {
      title: "Miras və vəsiyyətnamə",
      thumbnail: "../static/images/miras.jpeg",
      body: "",
      writer: "Vigdis Hjorth",
      old_price: 12,
      new_price: 21,
      count: 3,
      status: "active",
      category: "psixologiya",
    },
    {
      title: "1794",
      thumbnail: "../static/images/1974.jpg",
      body: "",
      writer: "Никлас Натт-о-Даг",
      old_price: 12,
      new_price: 21,
      count: 3,
      status: "active",
      category: "bilim-kurgu",
    },
    {
      title: "Sherlock Gibi Düşünmek",
      thumbnail: "../static/images/sherlock.jpg",
      body: "",
      writer: "Daniel Smith",
      old_price: 12,
      new_price: 21,
      count: 3,
      status: "active",
      category: "roman",
    },

  ];

  var filterFns = {
    numberGreaterThan50: function () {
      var number = $(this).find(".number").text();
      return parseInt(number, 10) > 50;
    },
    ium: function () {
      var name = $(this).find(".name").text();
      return name.match(/ium$/);
    },
  };

  $(".filter-button-group").on("click", "button", function () {
    var $grid = $(".grid").isotope({
      itemSelector: ".cols",
      layoutMode: "fitRows",
    });
    // use filterFn if matches value
    var filterValue = $(this).attr("data-filter");
    filterValue = filterFns[filterValue] || filterValue;
    $grid.isotope({ filter: filterValue });
  });

  let arr = [];

  let limitedCount = 0;
  $("#plus-btn").click(function () {
    if (limitedCount == products.length) return;
    limitedCount++;

    //   let inputValue = parseInt($('.inputCount').val())
    $(".inputCount").val(function (index, item) {
      if (products.length > parseInt(item)) {
        return parseInt(item) + 1;
      }
    });

    let randomInteger = getRandomInteger(0, products.length);
    console.log(randomInteger);

    while (arr.indexOf(randomInteger) > -1) {
      // tekrar eyni random reqem gelmemesi ucun while

      randomInteger = getRandomInteger(0, products.length);
      // if (arr.indexOf(randomInteger))
    }
    arr.push(randomInteger);
    console.log(`arr ${arr}`);

    if (arr.indexOf(randomInteger) > -1) {
      console.log(`random: ${typeof randomInteger}`);
      renderDom(randomInteger);
      randCount = randomInteger;
    } else {
      return;
    }
  });

  $("#minus-btn").click(function () {
    limitedCount--;
    if (limitedCount < 0) {
      limitedCount = 0;
    }

    $(".cols:last-child").remove(); // minus olduqca sondan silir

    $(".inputCount").val(function (index, item) {
      let count = parseInt(item) - 1;
      arr.pop(count);
      if (count >= 0) {
        return count;
      } else {
        return 0;
      }
    });
  });

  function getRandomInteger(min, max) { // Random integer almaq ucun function
    return Math.floor(Math.random() * (max - min) + min);
  }

  // tekrarlanmamagi ucun
  function neRepeat(int) {
    let arr = [];

    arr.push(int);
    arr = arr.set();
  }

  function renderDom(randomInt) {
    let title = products[randomInt].title;
    title = title.split(" ", 1);
    $(".page-content").append(`
        <div class="col-4 cols ${products[randomInt].category}">
        <div class="d-flex flex-column align-items-center body">
            <div class="card mb-5" style="width: 14rem;">
                <img src="${products[randomInt].thumbnail}" class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">${title}</h5>
                <p class="card-text">${products[randomInt].writer}</p>
                <a href="#" class="btn btn-info">Ətraflı</a>
                </div>
            </div>
        </div>
        `);
  }

  $(".start-btn").on("click", function (event) {
    // Basla button function

    event.preventDefault();
    if ($(this).hasClass("btn-warning")) {
      $(this).removeClass("btn-warning");
      $(this).addClass("btn-danger");
      $(this).html("Bitir");
      $(".start-btn-content").show();
    } else {
      $(".start-btn-content").hide();
      $(this).removeClass("btn-danger");
      $(this).addClass("btn-warning");
      $(this).html("Başla");
      $(".show-alert").find("#alert:first-child").remove();
    }
  });

  $(".start-calculate-btn").on("click", function () {
    let pageCount = $(".start-page-count").val();
    let dayCount = $(".start-day-count").val();

    showAlert(pageCount, dayCount);
    $(".start-page-count").val("");
    $(".start-day-count").val("");
  });
  function showAlert(value1, value2) {
    let result = 0;
    let alertBox = $(".show-alert");

    // alertBox.find("#alert:first-child").remove();
    if (
      !isNaN(value1) &&
      !isNaN(value2) &&
      parseInt(value2) != 0 &&
      parseInt(value1) >= parseInt(value2)
    ) {
      result = value1 / value2;
      alertBox.html(`
        <div id="alert" class="alert alert-success text-center p-3 mb-5 page-end-alert" role="alert"">
            Hər gün ən az <span class="h4 start-alert-page">${parseInt(
              result
            )}</span> səhifə oxumalısınız!
        </div>
      `);
    } else {
      $(".show-alert").html(`
          <div id="alert" class="alert alert-danger text-center p-3 mb-5 page-end-alert" role="alert">
          Hesablamada xəta baş verdi!
          </div>
        `);
    }
  }

  // $(".slider").slick({
  //   arrows: true,
  //   dots: true,
  //   infinite: true,
  //   slidesToShow: 3,
  //   slidesToScroll: 2
  // })
});
